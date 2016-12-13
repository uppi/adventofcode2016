import re

CONTROL_SEQ = re.compile("\((\d+)x(\d+)\)")

def expand(input_str):
    input_str = input_str.strip()
    score = 0
    while input_str:
        match = CONTROL_SEQ.search(input_str)
        if match is None:
            return score + len(input_str)
        else:
            score += match.start()
            char_cnt, times = map(int, match.groups())
            if(len(input_str) < char_cnt):
                print("Wtf? {} < {}", input_str, char_cnt)
            score += char_cnt * times
            input_str = input_str[match.end() + char_cnt:]
    return score


def expand_multiple(input_str):
    input_str = input_str.strip()
    score = 0
    while input_str:
        match = CONTROL_SEQ.search(input_str)
        if match is None:
            return score + len(input_str)
        else:
            score += match.start()
            char_cnt, times = map(int, match.groups())
            if(len(input_str) < char_cnt):
                print("Wtf? {} < {}", input_str, char_cnt)
            score += expand_multiple(input_str[match.end():match.end() + char_cnt]) * times
            input_str = input_str[match.end() + char_cnt:]
    return score

def expand_seq(seq):
    result = 0
    for s in seq:
        result += expand(s)
    return result

if __name__ == '__main__':
    with open("data/9.txt") as inp:
        input_str = "".join(inp)
        print(expand(input_str))
        print(expand_multiple(input_str))
