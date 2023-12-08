module Main where

import Data.List qualified as L
import Data.Map qualified as M
import Data.Maybe (fromJust)
import Data.Ord

parse :: [String] -> [(String, Int)]
parse = map (\l -> let [hand, bid] = words l in (hand, read bid))

cardOrder1 = M.fromList $ zip "23456789TJQKA" [0 ..]

cardOrder2 = M.fromList $ zip "J23456789TQKA" [0 ..]

sortedCardCounts :: (Ord a) => [a] -> [(a, Int)]
sortedCardCounts cs = L.sortBy (comparing $ Down . snd) counts
  where
    counts = map (\xs@(c : _) -> (c, length xs)) $ L.group $ L.sort cs

compareOr :: (Ord a) => a -> a -> Ordering -> Ordering
compareOr a b fallback = case compare a b of
  EQ -> fallback
  x -> x

compareCards :: String -> String -> M.Map Char Int -> Ordering
compareCards "" "" _ = EQ
compareCards (c1 : cs1) (c2 : cs2) order = compareOr (strength c1) (strength c2) (compareCards cs1 cs2 order)
  where
    strength c = fromJust $ M.lookup c order

compareHands :: String -> String -> Ordering
compareHands a b = compareOr counts1 counts2 $ compareCards a b cardOrder1
  where
    counts1 = map snd $ sortedCardCounts a
    counts2 = map snd $ sortedCardCounts b

compareHandsWithJoker :: String -> String -> Ordering
compareHandsWithJoker a b = compareOr counts1 counts2 $ compareCards a b cardOrder2
  where
    popJokerCount cs = case break ((== 'J') . fst) cs of
      (_, []) -> Nothing
      (left, (_, jokerCount) : right) -> Just (jokerCount, map snd $ left ++ right)
    resolveCounts cs = case popJokerCount cs of
      Nothing -> map snd cs
      Just (jokerCount, []) -> pure jokerCount
      Just (jokerCount, c : cs) -> (c + jokerCount) : cs
    resolve = resolveCounts . sortedCardCounts
    counts1 = resolve a
    counts2 = resolve b

winnings :: (String -> String -> Ordering) -> [(String, Int)] -> Int
winnings cmp hands = sum $ zipWith (*) (map snd ranked) [1 ..]
  where
    ranked = L.sortBy (\(a, _) (b, _) -> cmp a b) hands

main :: IO ()
main = do
  inp <- getContents
  let ls = lines inp
  let hands = parse ls
  print $ winnings compareHands hands
  print $ winnings compareHandsWithJoker hands