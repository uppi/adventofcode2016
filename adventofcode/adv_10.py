import re
import collections

PARSER_GIVE = re.compile("bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")
PARSER_GO = re.compile("value (\d+) goes to bot (\d+)")

def parse_input(input_seq):
    for cmd in input_seq:
        give_match = PARSER_GIVE.match(cmd)
        if give_match is not None:
            bot_id, type_a, a, type_b, b = give_match.groups()
            yield("give", int(bot_id), type_a == "bot", int(a), type_b == "bot", int(b))
        else:
            go_match = PARSER_GO.match(cmd)
            a, b = go_match.groups()
            yield("go", int(a), int(b))

def find_who_checks(seq, values_to_be_checked):
    state = collections.defaultdict(list)
    rules = {}
    outputs = {}

    for cmd in seq:
        if cmd[0] == "give":
            bot, low_receiver_is_bot, low_receiver, high_receiver_is_bot, high_receiver = cmd[1:]
            rules[bot] = (low_receiver_is_bot, low_receiver, high_receiver_is_bot, high_receiver)
        else:
            val, bot = cmd[1:]
            state[bot].append(val)

    while True:
        for key, value in list(state.items()):
            if len(value) == 2:
                if key in rules:
                    bot, vals = give(state, outputs, key, *rules[key])
                    if values_to_be_checked == vals:
                        return bot
                    break
    return None

def multiply_values(seq, needed_outs):
    state = collections.defaultdict(list)
    rules = {}
    outputs = {}

    for cmd in seq:
        if cmd[0] == "give":
            bot, low_receiver_is_bot, low_receiver, high_receiver_is_bot, high_receiver = cmd[1:]
            rules[bot] = (low_receiver_is_bot, low_receiver, high_receiver_is_bot, high_receiver)
        else:
            val, bot = cmd[1:]
            state[bot].append(val)

    while True:
        for key, value in list(state.items()):
            if len(value) == 2:
                if key in rules:
                    give(state, outputs, key, *rules[key])
                    if all(out in outputs for out in needed_outs):
                        res = 1
                        for out in needed_outs:
                            res *= outputs[out]
                        return res
                    break
    return None

def give(state, outputs, bot, low_receiver_is_bot, low_receiver, high_receiver_is_bot, high_receiver):
    low, high = tuple(sorted(state[bot]))
    if low_receiver_is_bot:
        state[low_receiver].append(low)
    else:
        outputs[low_receiver] = low
    if high_receiver_is_bot:
        state[high_receiver].append(high)
    else:
        outputs[high_receiver] = high
    state[bot] = list()
    return (bot, (low, high))

if __name__ == '__main__':
    with open("data/10.txt") as inp:
        inp_seq = list(inp)
        parsed_input = list(parse_input(inp_seq))
        print(find_who_checks(parsed_input, (17, 61)))
        print(multiply_values(parsed_input, (0, 1, 2)))
