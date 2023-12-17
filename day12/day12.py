with open("input.txt") as f:
    inputs = f.read().split("\n")[:-1]
inputs = list(
    map(
        lambda x: [
            x.split(" ")[0],
            tuple(map(lambda x: int(x), x.split(" ")[1].split(","))),
        ],
        inputs,
    )
)


mem = {}


def dfs(config, rules):
    print("Looking at: ", config, rules)
    # stopping conditions
    if config == "":
        return 1 if rules == () else 0
    if rules == ():
        return 1 if "#" not in config else 0
    if (config, rules) in mem:
        return mem[(config, rules)]

    result = 0
    if config[0] in ".?":
        result += dfs(config[1:], rules)
    if config[0] in "#?":
        result += (
            dfs(config[rules[0] + 1 :], rules[1:])
            if rules[0] <= len(config)
            and "." not in config[: rules[0]]
            and config[rules[0]] in ".?"
            else 0
        )
    mem[(config, rules)] = result
    return result


print(sum(map(lambda x: dfs(x[0] + ".", x[1]), inputs)))
