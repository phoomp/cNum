from casio.core.fractions import *

##### BEGIN GATHER #####


class Term:
    def __init__(self, coefficient=1, exponent=1, variable_name='x'):
        assert type(coefficient) == Fraction or type(coefficient) == int
        assert type(exponent) == Fraction or type(exponent) == int
        self.coefficient = coefficient
        self.exponent = exponent
        self.variable = variable_name

    def __add__(self, other):
        if self.exponent == other.exponent and self.variable == other.variable:
            return Term(coefficient=self.coefficient + other.coefficient, exponent=self.exponent)
        else:
            raise ValueError('Non-similar terms cannot be added.')

    def __sub__(self, other):
        if self.exponent == other.exponent and self.variable == other.variable:
            return Term(coefficient=self.coefficient + other.coefficient, exponent=self.exponent)
        else:
            raise ValueError('Non-similar terms cannot be subtracted.')

    def __mul__(self, other):
        return Term(coefficient=self.coefficient * other.coefficient, exponent=self.exponent + other.exponent)

    def __truediv__(self, other):
        return Term(coefficient=self.coefficient / other.coefficient, exponent=self.exponent - other.exponent)

    def __pow__(self, power):
        return Term(coefficient=self.coefficient ** power, exponent=self.exponent * power)

    def __str__(self):
        return str(self.coefficient) + str(self.variable) + '^' + str(self.exponent)
        # Python3 only
        # return f'{str(self.coefficient)}{self.variable}^{str(self.exponent)}'

##### END GATHER #####


def main():

    a = Term(Fraction(1, 3), 5)
    b = Term(13, 5)
    c = Term(15, 5)
    d = Term(14, 20)
    e = Term(Fraction(2, 29), 4)

    print(a)


if __name__ == '__main__':
    main()