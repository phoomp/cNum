# Lightweight Fractions Library for Python
# Created by Phoom Punpeng
# 2022-10-02

from math import comb, gcd


def similar(f1, f2):
    if type(f1) != Fraction or type(f2) != Fraction:
        raise TypeError('Arguments must be of type Fraction')


def factorial(n, limit=None):
    if (limit is not None and n <= limit) or (limit is None and n < 1):
        return 1
    elif type(n) == int:
        return n * factorial(n - 1, limit)
    elif type(n) == Fraction:
        return n * factorial(n - 1, limit)


def combination(n, r):
    assert (type(n) == int or type(n)) == Fraction
    assert type(r) == int or type(r) == Fraction and r >= 0

    # Type checking: r is a positive integer
    if type(r) == Fraction:
        assert r.isint()
        r = int(r.value)

    # Preparation: can we use Python's built-in function or not?
    n_isint = False
    n_use_builtin = False
    if type(n) == int or n.isint():
        n_isint = True
        n = int(n.value)
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
        factorial(3)


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

        # self.simplify()
        self.value = self.numerator / self.denominator
        self.exact_form = (self.numerator, self.denominator)

    def simplify(self):
        g = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // g, self.denominator // g)

    def __eq__(self, other, epsilon=1e-6):
        if type(other) == Fraction:
            return abs(self.numerator / self.denominator - other.numerator / other.denominator) < epsilon
        else:
            return abs(self.numerator / self.denominator - other) < epsilon

    def __le__(self, other):
        if type(other) == Fraction:
            return self.numerator / self.denominator <= other.numerator / other.denominator
        else:
            return self.numerator / self.denominator <= other

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

    def __pow__(self, power, modulo=None):
        return Fraction(self.numerator ** power, self.denominator ** power).simplify()

    def __str__(self):
        if self.is_int():
            return str(self.numerator // self.denominator)
        else:
            return f'{self.numerator}/{self.denominator}'

    def __abs__(self):
        self.numerator = abs(self.numerator)
        self.denominator = abs(self.denominator)
        return self

    def is_int(self):
        return self.numerator % self.denominator == 0


def main():
    print('Beginning Test')
    #
    # f1 = Fraction(1, 2, 3)
    # f2 = Fraction(1, 3)
    #
    # f4 = Fraction(1, 1)
    # f5 = Fraction(7, 8)
    # f6 = Fraction(1, 8)
    #
    # f7 = Fraction(2200000001, 700000000)
    # f8 = Fraction(22, 7)
    #
    # three = Fraction(3)
    #
    # print(f7)
    # print(f8)
    # print(f7 - f8)
    # print(f7 == f8)

    print(factorial(7, limit=5))

if __name__ == '__main__':
    main()
