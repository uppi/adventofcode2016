try:
    import queue
except:
    import Queue as queue
import hashlib
import sys

DIRECTIONS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}


_encode = lambda s: s

if sys.version_info >= (3, 0):
    _encode = lambda s: s.encode()


def directions(key, x, y, path):
    md5hash = hashlib.md5(
        _encode("{}{}".format(key, path))).hexdigest()[:4]
    #print(md5hash)
    for d, v in zip('UDLR', md5hash):
        if ord(v) >= ord('b'):
            sx, sy = DIRECTIONS[d]
            if x + sx >= 0 and y + sy >= 0 and x + sx < 4 and y + sy < 4:
                yield(x + sx, y + sy, path + d)


def path(key, start_x=0, start_y=0, end_x=3, end_y=3):
    q = queue.Queue()
    q.put((0, 0, ''))
    while not q.empty():
        x, y, path = q.get()
        #print(x, y, path)
        if x == end_x and y == end_y:
            return path
        for nx, ny, npath in directions(key, x, y, path):
            q.put((nx, ny, npath))


def longest_path_len(key, start_x=0, start_y=0, end_x=3, end_y=3):
    q = queue.Queue()
    longest_len = 0
    q.put((0, 0, ''))
    i = 0
    while not q.empty() and i < 10000:
        x, y, path = q.get()
        i = len(path)
        # print(x, y, path)
        if x == end_x and y == end_y:
            longest_len = max(longest_len, len(path))
        else:
            for nx, ny, npath in directions(key, x, y, path):
                q.put((nx, ny, npath))
    return longest_len


if __name__ == '__main__':
    print(path('pvhmgsws'))
    print(longest_path_len('pvhmgsws'))
