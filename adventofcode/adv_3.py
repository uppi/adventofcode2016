def parse_input(input_string):
    return [tuple(map(int, s.split())) for s in input_string.splitlines()]


def parse_colinput(input_string):
    next_three = [[], [], []]
    for s in input_string.splitlines():
        nums = map(int, s.split())
        for j, n in enumerate(nums):
            next_three[j].append(n)
        if len(next_three[0]) == 3:
            for n in next_three:
                yield tuple(n)
            next_three = [[], [], []]


def check_triangle(triangle):
    a, b, c = sorted(triangle)
    return a + b > c


def count_triangles(input_seq):
    result = 0
    for triangle in input_seq:
        if check_triangle(triangle):
            result += 1

    return result


if __name__ == '__main__':
    with open("data/3.txt") as inp:
        inp_str = inp.read()

        parsed_input = parse_input(inp_str)
        print(count_triangles(parsed_input))

        parsed_colinput = parse_colinput(inp_str)
        print(count_triangles(parsed_colinput))
