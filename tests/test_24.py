import unittest

import adventofcode.adv_24 as adv

SAMPLE_INPUT = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########""".splitlines()


class Test24(unittest.TestCase):
    def test_execute(self):
        self.assertEqual(14, adv.solve(SAMPLE_INPUT))
