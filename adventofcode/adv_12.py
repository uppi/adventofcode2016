import re

HEIGHT = 6
WIDTH = 50

PARSER = re.compile("(inc|dec|cpy|jnz) (-?\d+|[a-d]) ?(-?\d+|[a-d])?$")


def parse_input(input_seq):
    for cmd in input_seq:
        op, a, b = PARSER.match(cmd).groups()
        if not a.isalpha():
            a = int(a)
        if b is not None:
            if not b.isalpha():
                b = int(b)
            yield(op, (a, b))
        else:
            yield(op, (a,))


def inc(registers, reg):
    registers[reg] += 1
    registers["ip"] += 1


def dec(registers, reg):
    registers[reg] -= 1
    registers["ip"] += 1


def cpy(registers, value, reg):
    registers[reg] = registers.get(value, value)
    registers["ip"] += 1


def jnz(registers, value, offset):
    value = registers.get(value, value)
    offset = registers.get(offset, offset)
    if value != 0:
        registers["ip"] += offset
    else:
        registers["ip"] += 1


OP = {
    "jnz": jnz,
    "inc": inc,
    "dec": dec,
    "cpy": cpy,
}


def execute(code, **kwargs):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0, "ip": 0}
    registers.update(kwargs)
    while registers["ip"] < len(code):
        cmd, args = code[registers["ip"]]
        print(cmd, args)
        OP[cmd](registers, *args)

    return registers


if __name__ == '__main__':
    with open("data/12.txt") as inp:
        inp_seq = list(inp)
        parsed_input = list(parse_input(inp_seq))
        registers = execute(parsed_input, c=1)
        print(registers["a"])
