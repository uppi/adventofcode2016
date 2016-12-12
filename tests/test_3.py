import unittest

import adventofcode.adv_3 as adv


class Test3(unittest.TestCase):
    def test_input(self):
        parsed = adv.parse_input("1 2 3\n  145135       235423          234 ")
        self.assertEqual(
            [(1, 2, 3), (145135, 235423, 234)],
            parsed)

    def test_check_triangle(self):
        self.assertEqual(True, adv.check_triangle((12, 14, 16)))
        self.assertEqual(False, adv.check_triangle((10, 5, 25)))

    def test_count_triangles(self):
        parsed = adv.parse_input("")
        self.assertEqual(0, adv.count_triangles(parsed))

    def test_colinput(self):
        parsed = list(
            adv.parse_colinput("1 2 3\n  145135  235423  234 \n 21 23 35\n"
                               "4 5 6\n  745135  735423  734 \n 71 73 75\n"))
        self.assertEqual(
            [(1, 145135, 21), (2, 235423, 23), (3, 234, 35),
             (4, 745135, 71), (5, 735423, 73), (6, 734, 75)],
            parsed)
