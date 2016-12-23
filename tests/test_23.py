import unittest

import adventofcode.adv_23 as adv

SAMPLE_INPUT = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""".splitlines()


class Test12(unittest.TestCase):
    def test_execute(self):
        code = list(adv.parse_input(SAMPLE_INPUT))
        regs = adv.execute(code)
        self.assertEqual(3, regs["a"])
