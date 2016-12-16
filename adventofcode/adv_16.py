
def generate_state(state, desired_len):
    while len(state) < desired_len:
        b = "".join(str((int(s) + 1) % 2) for s in reversed(state))
        state = state + "0" + b
    return state[:desired_len]


def checksum(state):
    res = []
    f = True
    while f or len(state) % 2 == 0:
        f = False
        res = []
        for i in range(len(state) // 2):
            res.append(1 if state[i * 2] == state[i * 2 + 1] else 0)
        state = res
    return "".join(map(str, res))


if __name__ == '__main__':
    print(checksum(generate_state("10111100110001111", 272)))
    print(checksum(generate_state("10111100110001111", 35651584)))
