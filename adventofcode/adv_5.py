import hashlib


def search_md5(prefix):
    result = ""
    i = 0
    while True:
        md5hash = hashlib.md5("{}{}".format(prefix, i)).hexdigest()
        if md5hash.startswith("00000"):
            print(md5hash)
            result += md5hash[5]

            print("current result: ", result)
            if len(result) == 8:
                return result
        i += 1
        if i % 10000 == 0:
            print(i)


def search_md5_with_pos(prefix):
    result = [None, None, None, None, None, None, None, None]
    i = 0
    while True:
        md5hash = hashlib.md5("{}{}".format(prefix, i).encode()).hexdigest()
        i += 1
        if i % 500000 == 0:
            print(i)

        if md5hash.startswith("00000"):
            print(md5hash)
            pos = md5hash[5]
            if not pos.isdigit():
                continue
            pos = int(pos)
            if pos > 7:
                continue
            digit = md5hash[6]
            if result[pos] is None:
                result[pos] = digit
            print("current result: ", result)
            if all(x is not None for x in result):
                return "".join(result)


if __name__ == '__main__':
    # print(search_md5("ojvtpuvg"))
    print(search_md5_with_pos("ojvtpuvg"))
