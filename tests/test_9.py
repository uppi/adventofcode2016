import unittest

import adventofcode.adv_9 as adv

class Test9(unittest.TestCase):
    def test_expand(self):
        self.assertEqual(6, adv.expand("ADVENT"))
        self.assertEqual(7, adv.expand("A(1x5)BC"))
        self.assertEqual(9, adv.expand("(3x3)XYZ"))
        self.assertEqual(11, adv.expand("A(2x2)BCD(2x2)EFG"))
        self.assertEqual(6, adv.expand("(6x1)(1x3)A"))
        self.assertEqual(18, adv.expand("X(8x2)(3x3)ABCY"))

    def test_expand_multiple(self):
        self.assertEqual(9, adv.expand_multiple("(3x3)XYZ"))
        self.assertEqual(20, adv.expand_multiple("X(8x2)(3x3)ABCY"))
        self.assertEqual(241920, adv.expand_multiple("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
        self.assertEqual(445, adv.expand_multiple("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))