import unittest

import adventofcode.adv_7 as adv

SAMPLE_INPUT = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""".splitlines()

SAMPLE_INPUT_SSL = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""".splitlines()


class Test4(unittest.TestCase):
    def test_has_tls_support(self):
        self.assertTrue(adv.has_tls_support(SAMPLE_INPUT[0]))
        self.assertFalse(adv.has_tls_support(SAMPLE_INPUT[1]))
        self.assertFalse(adv.has_tls_support(SAMPLE_INPUT[2]))
        self.assertTrue(adv.has_tls_support(SAMPLE_INPUT[3]))

    def test_count_supporting_ips(self):
        self.assertEqual(
            2,
            adv.count_supporting_ips(SAMPLE_INPUT, adv.has_tls_support))
        self.assertEqual(
            3,
            adv.count_supporting_ips(SAMPLE_INPUT_SSL, adv.has_ssl_support))

    def test_has_ssl_support(self):
        self.assertTrue(adv.has_ssl_support(SAMPLE_INPUT_SSL[0]))
        self.assertFalse(adv.has_ssl_support(SAMPLE_INPUT_SSL[1]))
        self.assertTrue(adv.has_ssl_support(SAMPLE_INPUT_SSL[2]))
        self.assertTrue(adv.has_ssl_support(SAMPLE_INPUT_SSL[3]))
