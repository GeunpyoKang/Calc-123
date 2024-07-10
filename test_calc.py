from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_gop(self):
        calc = Calc()
        self.assertEqual(calc.getGop(2, 3), 6)