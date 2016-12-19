class FenvickTree():
    def __init__(self, size):
        self.data = [0] * size
        self.size = size
        for i in range(size):
            self.modify(i, 1)

    def sum(self, r):
        res = 0
        while r >= 0:

            res += self.data[r]
            r = (r & (r + 1)) - 1

        return res

    def modify(self, i, delta):
        while i < self.size:
            self.data[i] += delta
            i = (i | (i + 1))

    def sum2(self, l, r):
        res = self.sum(r) - self.sum(l - 1)
        return res

    def val(self, idx):
        if idx == 0:
            return self.sum(0)
        else:
            return self.sum2(idx, idx)


def solve(num):
    elves = [1] * num
    cur = 0
    while True:
        if elves[cur] != 0:
            other = (cur + 1) % num
            while elves[other] == 0:
                other = (other + 1) % num
            if other == cur:
                return cur + 1
            else:
                elves[cur] += elves[other]
                elves[other] = 0
                cur = (other + 1) % num
        else:
            cur = (cur + 1) % num


def solve_fen(num):
    elves = list(range(num))
    fenv = FenvickTree(num)

    cur = 0
    while True:
        if fenv.val(cur) != 0:
            if num % 1000 == 0:
                print(num)
            if num == 1:
                return cur + 1
            shift = (num // 2)
            other = cur + 1
            while shift > 0:
                if other + shift >= len(elves):
                    shift -= fenv.sum2(other, len(elves) - 1)
                    other = 0
                if shift != 0:
                    old_shift = shift
                    shift -= fenv.sum2(other, other + shift - 1)
                    other += old_shift
            other = (other - 1 + len(elves)) % len(elves)
            fenv.modify(other, -1)
            num -= 1
        cur = (cur + 1) % len(elves)


if __name__ == '__main__':
    print(solve_fen(3012210))
