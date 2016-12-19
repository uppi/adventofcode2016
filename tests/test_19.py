import unittest

import adventofcode.adv_19 as adv


class Test17(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(3, adv.solve(5))

    def test_solve_fen(self):
        self.assertEqual(2, adv.solve_fen(5))
