def next_tile(left, center, right):
    return '^' if left != right else '.'


def next_row(row):
    r = ["."] + list(row) + ["."]
    for i in range(len(row)):
        yield next_tile(*r[i:i + 3])


def count_safe(row, line_count):
    res = 0
    for l in range(line_count):
        res += len([e for e in row if e == '.'])
        row = list(next_row(row))
    return res


if __name__ == '__main__':
    print(count_safe("^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^", 400000))
