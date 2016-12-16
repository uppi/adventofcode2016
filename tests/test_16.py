import unittest

import adventofcode.adv_16 as adv


class Test16(unittest.TestCase):
    def test_generate_state(self):
        self.assertEqual("100", adv.generate_state("1", 3))
        self.assertEqual("001", adv.generate_state("0", 3))
        self.assertEqual(
            "11111000000",
            adv.generate_state("11111", 11))
        self.assertEqual(
            "1111000010100101011110000",
            adv.generate_state("111100001010", 25))

    def test_checksum(self):
        self.assertEqual(
            "100",
            adv.checksum("110010110100"))
