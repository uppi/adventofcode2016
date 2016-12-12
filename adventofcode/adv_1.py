def parse_input(input_string):
    result = map(
        lambda ts:
        (-1 if ts[0] == "L" else 1, int(ts[1:])), input_string.split(", "))
    return result


def calculate_distance(input_seq):
    distances = [0, 0, 0, 0]
    current = 0

    for turn, dist in input_seq:
        current = (current + 4 + turn) % 4
        distances[current] += dist

    return abs(distances[0] - distances[2]) + abs(distances[1] - distances[3])


def calculate_distance_of_first_cross(input_seq):
    distances = [0, 0, 0, 0]
    current = 0

    points_visited = set([(0, 0)])
    for turn, dist in input_seq:
        current = (current + 4 + turn) % 4
        for i in range(dist):
            distances[current] += 1
            cur_xy = (distances[0] - distances[2], distances[1] - distances[3])
            if cur_xy in points_visited:
                return abs(cur_xy[0]) + abs(cur_xy[1])
            else:
                points_visited.add(cur_xy)

    return abs(distances[0] - distances[2]) + abs(distances[1] - distances[3])


if __name__ == '__main__':
    parsed_input = parse_input("L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4")
    print(calculate_distance(parsed_input))
    print(calculate_distance_of_first_cross(parsed_input))
