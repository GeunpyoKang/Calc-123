class Calc:
    def get_sum_sum(self, a, b, c):
        if type(a) != int or type(b) != int or type(c) != int:
            raise AttributeError

        return a + b + c
