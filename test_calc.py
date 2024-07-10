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
        self.assertEqual(self.sut.getGop(2, 3), 6)

    def test_getDivide(self):
        self.assertEqual(self.sut.getDivide(6, 2), 3)

    def test_getDivide_zeroDivision(self):
        self.assertEqual(self.sut.getDivide(6, 0), "ZeroDivisionError")

    def test_get_minus(self):
        pass
