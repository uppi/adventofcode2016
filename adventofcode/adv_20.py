MAX_IP = 4294967295


def solve(seq):
    not_allowed = list(sorted(tuple(map(int, s.split("-"))) for s in seq))

    first_cand = None
    allowed_count = 0
    cand = 0

    while cand <= MAX_IP:
        while not_allowed and cand >= not_allowed[0][0]:
            cand = max(not_allowed[0][1] + 1, cand)
            not_allowed = not_allowed[1:]
        if cand <= MAX_IP:
            if first_cand is None:
                first_cand = cand
            if not not_allowed:
                allowed_count += (MAX_IP - cand)
                break
            allowed_count += 1
            cand += 1
    return first_cand, allowed_count


if __name__ == '__main__':
    with open("data/20.txt") as inp:
        print(" ".join(map(str, solve(inp))))
