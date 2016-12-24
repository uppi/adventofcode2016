import re
import itertools
try:
    import queue
except:
    import Queue as queue

def solve(inp, go_back=False):
    ids = []

    needed_positions = []
    for i, line in enumerate(inp):
        for j, char in enumerate(line):
            if char not in ("#", "."):
                needed_positions.append((i, j))
                ids.append(char)

    distances = {}

    for pos in needed_positions:
        cur_id = inp[pos[0]][pos[1]]
        distances[cur_id] = {}
        visited = set()
        q = queue.Queue()
        visited.add(pos)
        q.put((pos, 0))

        while not q.empty():
            state, step_count = q.get()
            y, x = state
            for new_state in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                ny, nx = new_state
                if new_state not in visited:
                    visited.add(new_state)
                    if inp[ny][nx] != '#':
                        q.put((new_state, step_count + 1))
                    if inp[ny][nx] in ids:
                        distances[cur_id][inp[ny][nx]] = step_count + 1

    dist = 1000000000000000
    for perm in itertools.permutations([i for i in ids if i != '0']):
        perm = ['0'] + list(perm) + (['0'] if go_back else [])
        new_dist = 0
        for i in range(1, len(perm)):
            new_dist += distances[perm[i-1]][perm[i]]
        if new_dist < dist:
            dist = new_dist
    return dist



if __name__ == '__main__':
    with open("data/24.txt") as inp:
        print(solve(inp.read().splitlines()), True)
