import re
import collections

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
    state[0] = 1 # Elevator
    for i, floor in enumerate(floors):
        for kind, t in floor:
            idx = ((i + 1) +
                   (i * kind_count) * 2 +
                   kinds[kind] * 2 +
                   (1 if t == "g" else 0))
            print("idx for {} {} is {}".format(kind, t, idx))
            state[idx] = 1
    return tuple(state)



if __name__ == '__main__':
    with open("data/10.txt") as inp:
        inp_seq = list(inp)
        floors = parse_input(inp_seq)
