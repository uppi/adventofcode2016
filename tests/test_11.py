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
            (1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
            adv.construct_state(adv.parse_input(SAMPLE_INPUT)))

    def test_is_valid(self):
        self.assertTrue(adv.is_valid(adv.construct_state(
            [
                [("hydrogen", "m"), ("lithium", "m")],
                [("hydrogen", "g")],
                [("lithium", "g")],
                []
            ])))

        self.assertTrue(adv.is_valid(adv.construct_state(
            [
                [("lithium", "m")],
                [("hydrogen", "g"), ("hydrogen", "m")],
                [("lithium", "g")],
                []
            ])))

        self.assertTrue(adv.is_valid(adv.construct_state(
            [
                [("lithium", "m")],
                [("hydrogen", "g"), ("hydrogen", "m"), ("lithium", "g")],
                [],
                []
            ])))

        self.assertFalse(adv.is_valid(adv.construct_state(
            [
                [("lithium", "m")],
                [("hydrogen", "g")],
                [("lithium", "g"), ("hydrogen", "m")],
                []
            ])))

    def test_move(self):
        state = (1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
        self.assertIsNone(adv.move(state, -1, 0, None))
        self.assertIsNone(adv.move(state, 1, 1, None))
        self.assertEqual(
            (0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
            adv.move(state, 1, 0, None))
        self.assertIsNone(
            adv.move(state, 1, 0, 2))
        self.assertEqual(
            (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            adv.move(
                (1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                1, 0, 2))

    def test_search(self):
        state = adv.construct_state(adv.parse_input(SAMPLE_INPUT))
        end_state = tuple(
            [0] * (3 * len(state) // 4) +
            [1] * (len(state) // 4))
        self.assertEqual(11, adv.search(state, end_state))
