from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):

    def setUp(self):
        self.sut = Calc()

    def test_invalid_params_in_get_sum_sum(self):
        with self.assertRaises(AttributeError):
            self.sut.get_sum_sum('a', 'b', 'c')

    def test_get_sum_sum(self):
        self.assertEqual(self.sut.get_sum_sum(1, 2, 3), 6)
        
    def test_gop(self):
        calc = Calc()
        self.assertEqual(calc.getGop(2, 3), 6)

    def test_getDivide(self):
        calc = Calc()
        self.assertEqual(calc.getDivide(6, 2), 3)

    def test_getDivide_zeroDivision(self):
        calc = Calc()
        self.assertEqual(calc.getDivide(6, 0), "ZeroDivisionError")
        
    def test_zegop_case(self):
        calc = Calc()
        ret = calc.getZegop(2)
        self.assertEqual(ret, 4)
        ret = calc.getZegop(3)
        self.assertEqual(ret, 9)
        ret = calc.getZegop(12)
        self.assertEqual(ret, 144)