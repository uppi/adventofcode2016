import unittest

import adventofcode.adv_13 as adv

SAMPLE_INPUT = """.#.####.##
..#..#...#
#....##...
###.#.###.
.##..#..#.
..##....#.
#...##.###""".splitlines()

SAMPLE_SALT = 10

SAMPLE_INPUT_PATH = """.#.####.##
.O#..#...#
#OOO.##...
###O#.###.
.##OO#OO#.
..##OOOO#.
#...##.###""".splitlines()

SAMPLE_PATH_LENGTH = 11


class Test4(unittest.TestCase):
    def test_can_be_passed(self):
        for y in range(len(SAMPLE_INPUT)):
            for x in range(len(SAMPLE_INPUT[0])):
                self.assertEqual(
                    SAMPLE_INPUT[y][x] == ".",
                    adv.can_be_passed(x, y, SAMPLE_SALT))

    def test_path(self):
        path = adv.path(1, 1, 7, 4, SAMPLE_SALT)
        self.assertEqual(path[0][:2], (1, 1))
        self.assertEqual(path[-1][:2], (7, 4))

        self.assertEqual(SAMPLE_PATH_LENGTH, len(path) - 1)

        print(path)

        for px, py in path:
            self.assertEqual('O', SAMPLE_INPUT_PATH[py][px])

    def test_count(self):
        cnt = adv.location_count(1, 1, SAMPLE_SALT, 4)
        self.assertEqual(9, cnt)
