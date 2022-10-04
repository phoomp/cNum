##### BEGIN GATHER #####
from math import comb, gcd


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
        r = int(r)

    # Preparation: can we use Python's built-in function or not?
    n_isint = False
    n_use_builtin = False
    if type(n) == int or n.is_int():
        n_isint = True
        n = int(n)
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


class Fraction:
    def __init__(self, numerator, denominator=1, third=None):
        if denominator == 0:
            raise ValueError('Denominator cannot be 0')

        if third is None:
            self.numerator = numerator
            self.denominator = denominator
        else:
            self.numerator = numerator * third + denominator
            self.denominator = third

        self.exact_form = (self.numerator, self.denominator)

    def simplify(self):
        g = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // g, self.denominator // g)

    def __eq__(self, other, epsilon=1e-6):
        if type(other) == Fraction:
            return abs(self.numerator / self.denominator - other.numerator / other.denominator) < epsilon
        else:
            return abs(self.numerator / self.denominator - other) < epsilon

    def __lt__(self, other):
        if type(other) == Fraction:
            return self.numerator / self.denominator <= other.numerator / other.denominator
        else:
            return self.numerator / self.denominator <= other

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __add__(self, f2):
        if self.denominator == f2.denominator:
            return Fraction(self.numerator + f2.numerator, self.denominator).simplify()
        else:
            return Fraction(self.numerator * f2.denominator + f2.numerator * self.denominator,
                            self.denominator * f2.denominator).simplify()

    def __sub__(self, f2):
        if self.denominator == f2.denominator:
            return Fraction(self.numerator - f2.numerator, self.denominator).simplify()
        else:
            return Fraction(self.numerator * f2.denominator - f2.numerator * self.denominator,
                            self.denominator * f2.denominator).simplify()

    def __mul__(self, other):
        if type(other) == int:
            return Fraction(self.numerator * other, self.denominator).simplify()
        else:
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator).simplify()

    def __truediv__(self, other):
        if type(other) == int:
            return Fraction(self.numerator, self.denominator * other).simplify()
        else:
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator).simplify()

    def __floordiv__(self, other):
        return self.numerator // self.denominator

    def __pow__(self, power):
        return Fraction(self.numerator ** power, self.denominator ** power).__ensure__int()

    def root(self, n=2):
        return Fraction(self.numerator ** (1 / n), self.denominator ** (1 / n)).__ensure__int()

    def __str__(self):
        if self.is_int():
            return str(self.numerator // self.denominator)
        else:
            return f'{self.numerator}/{self.denominator}'

    def __int__(self):
        if not self.is_int():
            print(Warning('Fraction is not an integer'))

        return round(self.numerator / self.denominator)

    def __float__(self):
        return self.numerator / self.denominator

    def __abs__(self):
        self.numerator = abs(self.numerator)
        self.denominator = abs(self.denominator)
        return self

    def __ensure__int(self):
        while (int(self.numerator) != self.numerator) or (int(self.denominator) != self.denominator):
            self.numerator *= 10
            self.denominator *= 10

        self.numerator = int(self.numerator)
        self.denominator = int(self.denominator)
        return self.simplify()

    def is_int(self):
        return self.numerator % self.denominator == 0


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
        return f'{str(self.coefficient)}{self.variable}^{str(self.exponent)}'

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