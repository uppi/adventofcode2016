import unittest

import adventofcode.adv_15 as adv

SAMPLE_INPUT = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.""".splitlines()


class Test15(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(5, adv.solve(SAMPLE_INPUT))
