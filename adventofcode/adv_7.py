import re

ABBA = re.compile("([a-z])([a-z])\2\1")


def _is_abba(s):
    return (len(s) == 4 and s[0] == s[3] and s[1] == s[2] and s[0] != s[1])


def _is_aba(s):
    return (len(s) == 3 and s[0] == s[2] and s[0] != s[1] and
            "[" not in s and "]" not in s)


def has_tls_support(ip):
    has_abba = False
    currently_squared = False
    last_4 = []
    for c in ip:
        if c == "[":
            currently_squared = True
        elif c == "]":
            currently_squared = False

        last_4 = last_4[-3:] + [c]
        if _is_abba(last_4):
            if currently_squared:
                return False
            else:
                has_abba = True
    return has_abba


def has_ssl_support(ip):
    abas = set()
    babs = set()

    currently_squared = False
    last_3 = []
    for c in ip:
        if c == "[":
            currently_squared = True
        elif c == "]":
            currently_squared = False

        last_3 = last_3[-2:] + [c]
        if _is_aba(last_3):
            if currently_squared:
                babs.add((last_3[1], last_3[0]))
            else:
                abas.add((last_3[0], last_3[1]))
    return bool(abas.intersection(babs))


def count_supporting_ips(seq, checkfun):
    return len([ip for ip in seq if checkfun(ip)])


if __name__ == '__main__':
    with open("data/7.txt") as inp:
        input_data = list(inp)
        print(count_supporting_ips(input_data, has_tls_support))
        print(count_supporting_ips(input_data, has_ssl_support))
