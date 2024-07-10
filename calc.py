class Calc:
    def get_sum_sum(self, a, b, c):
        if type(a) is not int or type(b) is not int or type(c) is not int:
            raise AttributeError
        return a + b + c

    def getGop(self, op1, op2):
        return op1 * op2

    def getDivide(self, op1, op2):
        try:
            return op1 // op2
        except ZeroDivisionError:
            return "ZeroDivisionError"

    def get_minus(self, a, b):
        if type(a) is not int or type(b) is not int:
            raise AttributeError
        return a - b
