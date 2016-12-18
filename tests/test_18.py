import unittest

import adventofcode.adv_18 as adv


class Test17(unittest.TestCase):
    def test_safety(self):
        self.assertEqual('.^^^^', "".join(adv.next_row('..^^.')))
        self.assertEqual('^^..^', "".join(adv.next_row('.^^^^')))

    def test_count_safe(self):
        self.assertEqual(
            38,
            adv.count_safe('.^^.^.^^^^', 10))
