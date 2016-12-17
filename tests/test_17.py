import unittest

import adventofcode.adv_17 as adv


class Test17(unittest.TestCase):
    def test_path(self):
        self.assertEqual('DDRRRD', adv.path('ihgpwlah'))
        self.assertEqual('DDUDRLRRUDRD', adv.path('kglvqrro'))
        self.assertEqual(
            'DRURDRUDDLLDLUURRDULRLDUUDDDRR',
            adv.path('ulqzkmiv'))

    def test2(self):
        self.assertEqual(370, adv.longest_path_len('ihgpwlah'))
        # self.assertEqual(492, adv.longest_path_len('kglvqrro'))
        # self.assertEqual(
        #     830,
        #     adv.longest_path_len('ulqzkmiv'))
