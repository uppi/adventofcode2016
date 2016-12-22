import re
try:
    import queue
except:
    import Queue as queue

G_R = re.compile("([0-9]+)-y([0-9]+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)")
#Size  Used  Avail  Use


def solve(inp):
    nodes = [tuple(map(int, x)) for x in G_R.findall(inp)]
    print(nodes)
    avail = [(a, x, y) for (x, y, s, u, a, up) in nodes]
    use = [(u, x, y) for (x, y, s, u, a, up) in nodes]

    pair_count = 0

    for a, x, y in avail:
        for u, x1, y1 in use:
            if (x1 != x or y1 != y) and a >= u and u != 0:
                pair_count += 1

    return pair_count


def find_turns(node_mat):
    """
    node_mat is [[used, available, tainted]]
    """
    max_y = len(node_mat) - 1
    max_x = len(node_mat[0]) - 1
    turns_available = []
    for _y in range(max_y + 1):
        for _x in range(max_x + 1):
            u, a, t = node_mat[_y][_x]
            for ny in range(_y - 1, _y + 2):
                for nx in range(_x - 1, _x + 2):
                    if nx != _x and ny != _y:
                        continue
                    if nx >= 0 and nx <= max_x and ny >= 0 and ny <= max_y:
                        nu, na, nt = node_mat[ny][nx]
                        if nu == 0:
                            continue
                        if nu <= a:
                            #print("We may move {} to {}".format(nu, a))
                            turns_available.append((nx, ny, _x, _y))
                        elif nt != 0 and nt <= a:
                            print("We may move tainted {} to {}".format(nu, a))
                            turns_available.append((nx, ny, _x, _y))
    res = []
    # print(turns_available)
    for nx, ny, x, y in turns_available:
        nm = list((list(l) for l in node_mat))
        u, a, t = nm[y][x]
        nu, na, nt = nm[ny][nx]
        if nt == 0:
            nm[y][x] = (u + nu, a - nu, t)
            nm[ny][nx] = (0, na + nu, 0)
        else:
            nm[y][x] = (u + nt, a - nt, nt)
            nm[ny][nx] = (nu - nt, na + nt, 0)
        res.append(tuple(tuple(l) for l in nm))

    return res


def print_state(node_mat):
    for line in node_mat:
        print(" ".join("{}/{}{}".format(
            u, a, "*" if t != 0 else "") for (u, a, t) in line))


def solve2(inp):
    nodes = [tuple(map(int, x)) for x in G_R.findall(inp)]
    max_x = max(x for (x, y, s, u, a, up) in nodes)
    max_y = max(y for (x, y, s, u, a, up) in nodes)
    node_mat = []
    for _ in range(max_y + 1):
        node_mat.append([(0, 0)] * (max_x + 1))

    for (x, y, s, u, a, up) in nodes:
        node_mat[y][x] = (u, a, u if y == 0 and x == max_x else 0)

    for line in node_mat:
        print(" ".join("{}/{}{}".format(
            u, a, "*" if t != 0 else "") for (u, a, t) in line))

    for line in node_mat:
        print("".join("{}".format(
            'G' if t!= 0 else '_' if u == 0 else '.' if u + a < 100 else '#') for (u, a, t) in line))

    q = queue.Queue()
    state = tuple(tuple(l) for l in node_mat)
    q.put((state, 0))
    been_there = set()
    been_there.add(state)
    prev_turns = 0
    while not q.empty():
        state, turns = q.get_nowait()
        if turns != prev_turns:
            print(turns)
            prev_turns = turns

        states = find_turns(state)
        for s in states:
            if s[0][0][2] != 0:
                return turns + 1
            if s not in been_there:
                been_there.add(s)
                #print_state(s)
                #print()
                q.put((s, turns + 1))


if __name__ == '__main__':
    with open("data/22.txt") as inp:
        print(solve2(inp.read()))
