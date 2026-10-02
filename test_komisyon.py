"""Komisyonun kendi kendini denetlemesi. Gecmezse lamba degil, yazilim yanar."""

import unittest

from komisyon import hukum, sonme_olasiligi


class TestKomisyon(unittest.TestCase):
    def test_aralik(self):
        p = sonme_olasiligi(7, 2, 15)
        self.assertGreater(p, 0.01)
        self.assertLess(p, 0.99)

    def test_uzun_sure_daha_soner(self):
        kisa = sonme_olasiligi(0.2, 0, 15)
        uzun = sonme_olasiligi(30, 4, 15)
        self.assertGreater(uzun, kisa)

    def test_hukum_bos_degil(self):
        self.assertTrue(hukum(0.9))
        self.assertTrue(hukum(0.2))


if __name__ == "__main__":
    unittest.main()
