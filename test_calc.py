from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_gop(self):
        calc = Calc()
        self.assertEqual(calc.getGop(2, 3), 6)

    def test_getDivide(self):
        calc = Calc()
        self.assertEqual(calc.getDivide(6, 2), 3)

    def test_getDivide_zeroDivision(self):
        calc = Calc()
        self.assertEqual(calc.getDivide(6, 0), "ZeroDivisionError")
