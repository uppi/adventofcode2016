import unittest

import adventofcode.adv_2 as adv


class Test2(unittest.TestCase):
    def test_input(self):
        parsed = adv.parse_input("LLUUUU\nLLRRRR\nR\nD")
        self.assertEqual(
            [
                ((-1, 0), (-1, 0), (0, -1), (0, -1), (0, -1), (0, -1)),
                ((-1, 0), (-1, 0), (1, 0), (1, 0), (1, 0), (1, 0)),
                ((1, 0),),
                ((0, 1),)],
            parsed)

    def test_calculate_code(self):
        parsed = adv.parse_input("ULL\nRRDDD\nLURDL\nUUUUD")
        code = adv.calculate_code(parsed)
        self.assertEqual("1985", code)
