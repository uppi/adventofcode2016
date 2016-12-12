import unittest

import adventofcode.adv_4 as adv


class Test4(unittest.TestCase):
    def test_input(self):
        parsed = adv.parse_input(
            "aaaaa-bbb-z-y-x-123[abxyz]\ntotally-real-room-200[decoy]")
        self.assertEqual(
            [(("aaaaa", "bbb", "z", "y", "x"), 123, "abxyz"),
             (("totally", "real", "room"), 200, "decoy")],
            list(parsed))

    def test_checksum(self):
        parsed = adv.parse_input(
            "aaaaa-bbb-z-y-x-123[abxyz]\ntotally-real-room-200[decoy]")
        correct, incorrect = parsed
        self.assertTrue(adv.check_checksum(correct[0], correct[2]))
        self.assertFalse(adv.check_checksum(incorrect[0], incorrect[2]))

    def test_sum_valid_sectors(self):
        parsed = adv.parse_input("aaaaa-bbb-z-y-x-123[abxyz]\n"
                                 "a-b-c-d-e-f-g-h-987[abcde]\n"
                                 "not-a-real-room-404[oarel]\n"
                                 "totally-real-room-200[decoy]")
        self.assertEqual(1514, adv.sum_valid_sectors(parsed))

    def test_decrypt(self):
        name, sector, checksum = list(adv.parse_input(
            "qzmt-zixmtkozy-ivhz-343[lol]"))[0]
        self.assertEqual(
            ("very encrypted name"),
            adv.decrypt(name, sector))
