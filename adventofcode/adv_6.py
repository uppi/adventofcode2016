import collections


def correct_message(seq):
    counters = None
    for msg in seq:
        msg = msg.strip()
        if counters is None:
            counters = []
            for ch in msg:
                counters.append(collections.Counter(ch))
        else:
            for i, ch in enumerate(msg):
                counters[i].update(ch)
    return "".join(c.most_common(1)[0][0] for c in counters)


def modified_correct_message(seq):
    counters = None
    for msg in seq:
        msg = msg.strip()
        if counters is None:
            counters = []
            for ch in msg:
                counters.append(collections.Counter(ch))
        else:
            for i, ch in enumerate(msg):
                counters[i].update(ch)
    return "".join(c.most_common()[-1][0] for c in counters)


if __name__ == '__main__':
    with open("data/6.txt") as inp:
        input_data = list(inp)
        print(correct_message(input_data))
        print(modified_correct_message(input_data))
