import re

PARSER = re.compile("Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).")

def parse(seq_elem):
    disc, pos_count, cur_pos = PARSER.match(seq_elem).groups()
    return map(int, (disc, pos_count, cur_pos))

def solve(seq):
    discs_shifted = []
    for elem in seq:
        disc, pos_count, cur_pos = parse(elem)
        discs_shifted.append((cur_pos + disc, pos_count))

    for i in range(100000000):
        if check_shifted(discs_shifted):
            return i
        discs_shifted = turn_shifted(discs_shifted)
    return None

def turn_shifted(d_shifted):
    return [((x + 1) % y, y) for x, y in d_shifted]

def check_shifted(d_shifted):
    for x, y in d_shifted:
        if x != 0:
            return False
    return True

if __name__ == '__main__':
    with open("data/15_2.txt") as inp:
        print(solve(inp))
