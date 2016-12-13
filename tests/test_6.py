import unittest

import adventofcode.adv_6 as adv

SAMPLE_INPUT = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".splitlines()


class Test4(unittest.TestCase):
    def test_correct(self):
        self.assertEqual("easter", adv.correct_message(SAMPLE_INPUT))

    def test_modified_correct(self):
        self.assertEqual("advent", adv.modified_correct_message(SAMPLE_INPUT))
