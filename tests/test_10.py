import unittest

import adventofcode.adv_10 as adv

SAMPLE_INPUT = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2""".splitlines()

class Test10(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(
            [("go", 5, 2),
             ("give", 2, True, 1, True, 0),
             ("go", 3, 1),
             ("give", 1, False, 1, True, 0),
             ("give", 0, False, 2, False, 0),
             ("go", 2, 2)],
            list(adv.parse_input(SAMPLE_INPUT)))


    def test_find_who_checks(self):
        self.assertEqual(
            2,
            adv.find_who_checks(
                adv.parse_input(SAMPLE_INPUT),
                (2, 5)))