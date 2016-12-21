import unittest

import adventofcode.adv_21 as adv

INPUT = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d""".splitlines()


class Test21(unittest.TestCase):
    def test_solve(self):
        self.assertEqual("decab", adv.solve("abcde", INPUT))
        self.assertEqual(
            "abcde", adv.solve_reverse("decab", reversed(INPUT)))
