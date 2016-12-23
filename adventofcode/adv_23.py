import re

HEIGHT = 6
WIDTH = 50

PARSER = re.compile("(inc|dec|cpy|jnz|tgl) (-?\d+|[a-d]) ?(-?\d+|[a-d])?$")


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


def tgl(code, registers, value):
    value = registers.get(value, value)
    value = registers["ip"] + value
    print("should toggle ", value)
    if value >= len(code):
        registers["ip"] += 1
        return
    if value == registers["ip"]:
        print("Thats us")
        registers["ip"] += 1
        return
    instr = code[value]
    print("Instr is", instr)
    if instr[0] == "inc":
        instr = tuple(["dec"] + list(instr[1:]))
    elif instr[0] == "dec":
        instr = tuple(["inc"] + list(instr[1:]))
    elif instr[0] == "tgl":
        instr = tuple(["inc"] + list(instr[1:]))
    elif instr[0] == "jnz":
        print(instr)
        if instr[1][1] in ("a", "b", "c", "d"):
            instr = tuple(["cpy"] + list(instr[1:]))
    elif instr[0] == "cpy":
        instr = tuple(["jnz"] + list(instr[1:]))
    code[value] = instr
    registers["ip"] += 1


def inc(code, registers, reg):
    # optimize_inc_dec_jnz(code, registers)
    registers[reg] += 1
    registers["ip"] += 1


def dec(code, registers, reg):
    registers[reg] -= 1
    registers["ip"] += 1


def cpy(code, registers, value, reg):
    registers[reg] = registers.get(value, value)
    registers["ip"] += 1


def jnz(code, registers, value, offset):
    if registers.get(value, value) != 0:
        registers["ip"] += registers.get(offset, offset)
    else:
        registers["ip"] += 1


OP = {
    "jnz": jnz,
    "inc": inc,
    "dec": dec,
    "cpy": cpy,
    "tgl": tgl
}


def execute(code, **kwargs):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0, "ip": 0}
    registers.update(kwargs)
    c = 0
    while registers["ip"] < len(code):
        c += 1
        if c % 1000 == 1:
            print(registers)
        cmd, args = code[registers["ip"]]
        OP[cmd](code, registers, *args)

    return registers


if __name__ == '__main__':
    with open("data/23.txt") as inp:
        inp_seq = list(inp)
        parsed_input = list(parse_input(inp_seq))
        registers = execute(parsed_input, a=12)
        print(registers["a"])
