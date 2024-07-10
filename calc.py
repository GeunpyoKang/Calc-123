class Calc:
    def get_sum_sum(self, a, b, c):
        if type(a) is not int or type(b) is not int or type(c) is not int:
            raise AttributeError

        return a + b + c
