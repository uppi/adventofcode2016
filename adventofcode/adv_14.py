import hashlib
import re
import sys

CAND = re.compile("([a-z0-9])\\1\\1")
KEY = re.compile("([a-z0-9])\\1\\1\\1\\1")


_encode = lambda s: s

if sys.version_info >= (3, 0):
    _encode = lambda s: s.encode()


def find_64key(prefix, stratch=False):
    i = 0
    candidates = []
    cur_keys = []
    stop_searching = False
    while (not stop_searching or candidates):
        md5hash = hashlib.md5(_encode("{}{}".format(prefix, i))).hexdigest()
        if stratch:
            for _ in range(2016):
                md5hash = hashlib.md5(_encode(md5hash)).hexdigest()
        for key in KEY.findall(md5hash):
            for c, start_idx in candidates:
                if c == key and i - start_idx < 1000:
                    cur_keys.append((start_idx, i - start_idx))
                    cur_keys = sorted(cur_keys)
                    print("adding {} from {} at {} => {}".format(
                        c, start_idx, i, len(cur_keys)))
                    if len(cur_keys) >= 64:
                        stop_searching = True
            candidates = [(c, start_idx) for (c, start_idx) in candidates
                          if c != key and i - start_idx < 1000]
        if not stop_searching:
            for cand in CAND.findall(md5hash):
                candidates.append((cand, i))
                break
        i += 1
        if i % 10000 == 0:
            print(i)
    return cur_keys[63][0]

if __name__ == '__main__':
    print(find_64key("ngcjuoqr", True))
