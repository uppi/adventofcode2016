import unittest

import adventofcode.adv_20 as adv

INPUT = """5-8
0-2
4-7""".splitlines()


class Test17(unittest.TestCase):
    def test_solve(self):
        allowed_first, allowed_len = adv.solve(INPUT)
        self.assertEqual(3, allowed_first)
        self.assertEqual(4294967295 - 8, allowed_len)
