from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):

    def test_gop_case(self):
        calc = Calc()
        ret = calc.getGop(2, 5)
        self.assertEqual(ret, 10)
        ret = calc.getGop(2, 7)
        self.assertEqual(ret, 14)
        ret = calc.getGop(28, 5)
        self.assertEqual(ret, 140)
        ret = calc.getGop(13, 3)
        self.assertEqual(ret, 39)

    def test_zegop_case(self):
        calc = Calc()
        ret = calc.getZegop(2)
        self.assertEqual(ret, 4)
        ret = calc.getZegop(3)
        self.assertEqual(ret, 9)
        ret = calc.getZegop(12)
        self.assertEqual(ret, 144)
