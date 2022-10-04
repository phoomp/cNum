from casio.core.fractions import *

##### BEGIN GATHER #####


def similar(f1, f2):
    if type(f1) != Fraction or type(f2) != Fraction:
        raise TypeError('Arguments must be of type Fraction')


def factorial(n, limit=None):
    if (limit is not None and n <= limit) or (limit is None and n < 1):
        return 1
    else:
        return n * factorial(n - 1, limit)


def combination(n, r):
    assert type(n) == int or type(n) == Fraction
    assert type(r) == int or type(r) == Fraction and r >= 0

    # Type checking: r is a positive integer
    if type(r) == Fraction:
        assert r.is_int()
        # r = int(r)
        r = r.get_int()

    # Preparation: can we use Python's built-in function or not?
    n_isint = False
    n_use_builtin = False
    if type(n) == int or n.is_int():
        n_isint = True
        # n = int(n)
        n = n.get_int()

        if n >= 0:
            n_use_builtin = True

    # Special cases, no need to calculate any further
    if r == 0:
        if n_isint:
            return 1
        else:
            return Fraction(1)

    if n == 0:
        if n_isint:
            return 0
        else:
            return Fraction(0)

    if r == 1:
        return n

    # Calculate the combination

    # If n is an integer, we can use Python's built-in function
    if n_use_builtin:
        return comb(n, r)
    else:
        # Use the formula for combinations
        return factorial(n, limit=n - r) / factorial(r)


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

    print((a * (b + c) * d) / e)


if __name__ == '__main__':
    main()