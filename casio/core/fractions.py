# Lightweight Fractions Library for Python
# Created by Phoom Punpeng
# 2022-10-02

from math import comb, gcd


def similar(f1, f2):
    if type(f1) != Fraction or type(f2) != Fraction:
        raise TypeError('Arguments must be of type Fraction')


def combination(n, r):
    assert (type(n) == int or type(n) == Fraction) and n != 0
    assert type(r) == int or type(r) == Fraction

    if type(r) == Fraction:
        assert r.isint()
        r = int(r.value)  # Don't use the numerator, denominator might not be 0

    if type(n) == int and n > 0:
        return comb(n, r)  # Use Python's built-in combinations function

    if type(n) == int:
        pass

class Fraction:
    def __init__(self, numerator, denominator=1, third=None):
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
        return self.numerator / self.denominator - other.numerator / other.denominator < epsilon

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

    f1 = Fraction(1, 2, 3)
    f2 = Fraction(1, 3)

    f4 = Fraction(1, 1)
    f5 = Fraction(7, 8)
    f6 = Fraction(1, 8)

    f7 = Fraction(2200000001, 700000000)
    f8 = Fraction(22, 7)

    three = Fraction(3)

    print(f7)
    print(f8)
    print(f7 - f8)
    print(f7 == f8)


if __name__ == '__main__':
    main()
