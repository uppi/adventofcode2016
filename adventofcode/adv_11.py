import re
import collections
import queue

PARSER_GENERATOR = re.compile(" (\w+) generator")
PARSER_MICROCHIP = re.compile(" (\w+)-compatible microchip")


def parse_input(input_seq):
    floors = []
    for floor_state_str in input_seq:
        floor = []
        for mch in PARSER_MICROCHIP.findall(floor_state_str):
            floor.append((mch, "m"))
        for gen in PARSER_GENERATOR.findall(floor_state_str):
            floor.append((gen, "g"))
        floors.append(floor)
    return floors


def construct_state(floors):
    kinds = {}
    kind_count = 0
    for floor in floors:
        for kind, t in floor:
            if kind not in kinds:
                kinds[kind] = kind_count
                kind_count += 1
    state = [0] * (len(floors) + kind_count * 2 * len(floors))
    state[0] = 1  # Elevator
    for i, floor in enumerate(floors):
        for kind, t in floor:
            idx = ((i + 1) +
                   (i * kind_count) * 2 +
                   kinds[kind] * 2 +
                   (1 if t == "g" else 0))
            print("idx for {} {} is {}".format(kind, t, idx))
            state[idx] = 1
    return tuple(state)


def is_valid(state):
    floor_len = len(state) // 4
    for floor_idx in range(4):
        has_m_without_g = False
        has_g = False
        base = (floor_len * floor_idx) + 1
        for i in range((floor_len - 1) // 2):
            m = state[base + 2 * i]
            g = state[base + 2 * i + 1]
            if m and not g:
                has_m_without_g = True
            if g:
                has_g = True
            if has_m_without_g and has_g:
                return False
    return True


def move(state, direction, first, second):
    floor_len = len(state) // 4
    current_floor = 0
    for i in range(4):
        if state[floor_len * i] == 1:
            current_floor = i
            break

    if direction == -1 and current_floor == 0:
        return None
    if direction == 1 and current_floor == 3:
        return None

    if first > floor_len - 1:
        return None

    base = (floor_len * current_floor) + 1
    if state[base + first] != 1:
        return None

    if second is not None:
        if second > floor_len - 1:
            return None
        if state[base + second] != 1:
            return None

    desired_base = (floor_len * (current_floor + direction)) + 1

    to_change = list(state)
    to_change[base - 1] = 0
    to_change[desired_base - 1] = 1

    to_change[base + first] = 0
    to_change[desired_base + first] = 1
    if second is not None:
        to_change[base + second] = 0
        to_change[desired_base + second] = 1

    if is_valid(to_change):
        return tuple(to_change)

    return None


def search(start_state, end_state):
    visited = set()
    q = queue.Queue()
    visited.add(start_state)
    q.put((start_state, 0))

    floor_len = (len(start_state) // 4) - 1

    current_step_count = 0

    while not q.empty():
        state, step_count = q.get()

        if step_count > current_step_count:
            current_step_count = step_count
            print(current_step_count)

        for direction in (-1, 1):
            for first in range(floor_len):
                for second in [None] + list(range(first + 1, floor_len)):
                    try_state = move(state, direction, first, second)
                    if try_state is None:
                        continue
                    if try_state in visited:
                        continue
                    if try_state == end_state:
                        return step_count + 1
                    visited.add(try_state)
                    q.put((try_state, step_count + 1))
    return None


if __name__ == '__main__':
    with open("data/11_1.txt") as inp:
        inp_seq = list(inp)
        state = construct_state(parse_input(inp_seq))
        end_state = tuple(
            [0] * (3 * len(state) // 4) +
            [1] * (len(state) // 4))
        print(state)
        print(end_state)
        print(search(state, end_state))
