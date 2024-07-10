class Calc:
    def getGop(self, op1, op2):
        return op1 * op2

    def getDivide(self, op1, op2):
        try:
            return op1 // op2
        except ZeroDivisionError:
            return "ZeroDivisionError"

