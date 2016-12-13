import unittest

import adventofcode.adv_8 as adv

SAMPLE_INPUT = """rotate row y=0 by 6
rotate column x=0 by 1
rect 4x1""".splitlines()


class Test4(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(
            [("rotrow", 0, 6), ("rotcol", 0, 1), ("rect", 4, 1)],
            list(adv.parse_input(SAMPLE_INPUT)))

    def test_rotrow(self):
        display = [[1, 2, 3, 4], [5, 6, 7, 8]]
        adv.rotrow(display, 1, 3)
        self.assertEqual(
            [[1, 2, 3, 4], [6, 7, 8, 5]],
            display)

        display2 = [[0] * 50]
        display2[0][0] = 1
        adv.rotrow(display2, 0, 51)
        self.assertEqual(0, display2[0][0])
        self.assertEqual(1, display2[0][1])

    def test_rotcol(self):
        display2 = []
        for i in range(6):
            display2.append([0])
        display2[0][0] = 1
        adv.rotcol(display2, 0, 7)
        self.assertEqual(0, display2[0][0])
        self.assertEqual(1, display2[1][0])

    def test_rect(self):
        display = [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        adv.rect(display, 2, 3)
        self.assertEqual([[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]], display)

    def test_sample(self):
        display = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        turns = [("rect", 3, 2), ("rotcol", 1, 1),
                 ("rotrow", 0, 4), ("rotcol", 1, 1)]
        for cmd, a, b in turns:
            adv.OP[cmd](display, a, b, height=3, width=7)

        self.assertEqual(
            [[0, 1, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0]],
            display)

    def test_sample_2(self):
        turns = [("rect", 3, 2), ("rotcol", 1, 1),
                 ("rotrow", 0, 4), ("rotcol", 1, 1)]
        self.assertEqual(6, adv.count_lit(turns, height=3, width=7))
