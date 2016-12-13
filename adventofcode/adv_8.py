import re

HEIGHT = 6
WIDTH = 50

PARSER = re.compile("(rect |rotate row y=|rotate column x=)(\d+)(?:x| by )(\d+)")

FMT_OP = {
    "rect ": "rect",
    "rotate row y=": "rotrow",
    "rotate column x=": "rotcol"
}

def parse_input(input_seq):
    for cmd in input_seq:
        op, a, b = PARSER.match(cmd).groups()
        op, a, b = FMT_OP[op], int(a), int(b)
        yield(op, a, b)


def rect(display, a, b, **kwargs):
    for i in range(b):
        for j in range(a):
            display[i][j] = 1


def rotcol(display, col, turns, height=HEIGHT, **kwargs):
    newcol = [display[i][col] for i in range(height)]
    turns = turns % height
    newcol = newcol[-turns:] + newcol[:-turns]
    for i in range(height):
        display[i][col] = newcol[i]


def rotrow(display, row, turns, width=WIDTH, **kwargs):
    turns = turns % width
    display[row] = display[row][-turns:] + display[row][:-turns]

OP = {
    "rect": rect,
    "rotrow": rotrow,
    "rotcol": rotcol
}

def count_lit(seq, height=HEIGHT, width=WIDTH):
    display = []
    for i in range(height):
        display.append([0] * width)
    for cmd, arg1, arg2 in seq:
        OP[cmd](display, arg1, arg2, height=height, width=width)
    for line in display:
        print(" ".join(" " if elem == 0 else "#" for elem in line))
    return sum(sum(l) for l in display)


if __name__ == '__main__':
    with open("data/8.txt") as inp:
        inp_seq = list(inp)
        parsed_input = list(parse_input(inp_seq))
        print(count_lit(parsed_input))
