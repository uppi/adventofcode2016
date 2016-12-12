import unittest

import adventofcode.adv_1 as adv


class Test1(unittest.TestCase):
    def test_input(self):
        parsed = adv.parse_input("L1, R1, L3")
        self.assertEqual([(-1, 1), (1, 1), (-1, 3)], list(parsed))

        parsed2 = adv.parse_input("L1, R11, L3")
        self.assertEqual([(-1, 1), (1, 11), (-1, 3)], list(parsed2))

    def test_distance(self):
        distance = adv.calculate_distance([(-1, 1), (1, 1), (-1, 3), (-1, 3)])
        self.assertEqual(6, distance)

    def test_distance_of_first_cross(self):
        distance = adv.calculate_distance_of_first_cross(
            [(1, 8), (1, 4), (1, 4), (1, 8)])
        self.assertEqual(4, distance)
