import unittest

import adventofcode.adv_11 as adv

SAMPLE_INPUT = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.""".splitlines()

class Test11(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(
            [
                [("hydrogen", "m"), ("lithium", "m")],
                [("hydrogen", "g")],
                [("lithium", "g")],
                []],
            adv.parse_input(SAMPLE_INPUT))

    def test_construct_state(self):
        self.assertEqual(
            (1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0),
            adv.construct_state(adv.parse_input(SAMPLE_INPUT)))