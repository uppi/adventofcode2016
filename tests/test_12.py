import unittest

import adventofcode.adv_12 as adv

SAMPLE_INPUT = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""".splitlines()


class Test12(unittest.TestCase):
    def test_execute(self):
        code = list(adv.parse_input(SAMPLE_INPUT))
        regs = adv.execute(code)
        self.assertEqual(42, regs["a"])
