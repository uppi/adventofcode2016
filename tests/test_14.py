import unittest

import adventofcode.adv_14 as adv

SAMPLE_INPUT = "abc"


class Test12(unittest.TestCase):
    def test_solve(self):
        result = adv.find_64key(SAMPLE_INPUT)
        self.assertEqual(22728, result)
