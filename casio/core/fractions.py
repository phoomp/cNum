# Lightweight Fractions Library for Python
# Created by Phoom Punpeng
# 2022-10-02

from __future__ import division

##### BEGIN GATHER #####


# GCD Function, for Python 2
def gcd(a, b):
    # Find minimum of a and b
    result = min(a, b)

    if result < 10e5:
        while result:
            if a % result == 0 and b % result == 0:
                break
            result -= 1

    else:
        i = 10e5
        result = 1
        while i:
            if a % i == 0 and b % i == 0:
                result *= i
                a /= i
                b /= i

            i -= 1

    # Return the gcd of a and b
    return int(result)


def similar(f1, f2):
    if type(f1) != Fraction or type(f2) != Fraction:
        raise TypeError('Arguments must be of type Fraction')


def factorial(n, limit=None):
    if (limit is not None and n <= limit) or (limit is None and n < 1):
        return 1
    else:
        if isinstance(n, Fraction):
            # Get around Python 2's limitations
            return n.__mul__(factorial(n.__sub__(1), limit))
        else:
            return n * factorial(n - 1, limit)


# Python 2 substitute for Python 3's comb function
def comb(n, r):
    # nCr = n! / r!(n-r)!
    assert type(n) == int and type(r) == int

    n_fac = factorial(n)
    r_fac = factorial(r)
    n_r_fac = factorial(n - r)

    d = r_fac * n_r_fac

    return int(n_fac / d)


def combination(n, r):
    assert isinstance(n, int) or isinstance(n, Fraction)
    assert isinstance(r, int) or (isinstance(r, Fraction) and r.is_int())

    # Type checking: r is a positive integer
    if isinstance(r, Fraction):
        assert r.is_int()
        r = r.get_int()

    # Preparation: can we use Python's built-in function or not?
    n_isint = False
    n_use_builtin = False
    if type(n) == int or n.is_int():
        n_isint = True
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
        return Fraction(comb(n, r))
    else:
        # Use the formula for combinations
        if isinstance(n, Fraction):
            # return Fraction(factorial(n, limit=n.__sub__(r)).__truediv__(factorial(r)))
            return factorial(n, limit=n.__sub__(r)).__truediv__(factorial(r))
        else:
            return factorial(n, limit=n - r).__truediv__(factorial(r))


class Fraction:
    def __init__(self, numerator, denominator=1, third=None):
        if type(numerator) == str:
            assert denominator == 1 and third is None
            self.denominator = denominator
            self.parse(numerator)
        else:
            if denominator == 0:
                raise ValueError('Denominator cannot be 0')

            if third is None:
                self.numerator = numerator
                self.denominator = denominator
            else:
                self.numerator = numerator * third + denominator
                self.denominator = third

            self.exact_form = (self.numerator, self.denominator)

    def parse(self, s):
        try:
            if int(s) == float(s):
                self.numerator = int(s)
                return
        except Exception as e:
            pass

        try:
            if float(s) == s:
                self.numerator = s
                self.__ensure__int()
                return
        except Exception as e:
            pass
        try:
            if '/' in s:
                assert s.count('/') == 1
                s = s.split('/')
                self.numerator = float(s[0])
                self.denominator = float(s[1])
                self.__ensure__int()
                return
        except Exception as e:
            pass

        raise ValueError('Unsupported value: ' + s)

    def simplify(self):
        if self.numerator == 0 or self.denominator == 1:
            return self

        g = gcd(abs(self.numerator), abs(self.denominator))
        assert self.numerator % g == 0 and self.denominator % g == 0
        return Fraction(int(self.numerator / g), int(self.denominator / g))

    def __eq__(self, other, epsilon=1e-6):
        if isinstance(other, Fraction):
            return abs(self.numerator / self.denominator - other.numerator / other.denominator) < epsilon
        else:
            return abs(self.numerator / self.denominator - other) < epsilon

    def __lt__(self, other):
        if isinstance(other, Fraction):
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
        if type(f2) == float or type(f2) == int:
            f2 = Fraction(f2).__ensure__int()

        if self.denominator == f2.denominator:
            return Fraction(self.numerator + f2.numerator, self.denominator).simplify()
        else:
            return Fraction(self.numerator * f2.denominator + f2.numerator * self.denominator,
                            self.denominator * f2.denominator).simplify()

    def __sub__(self, f2):
        if type(f2) == float or type(f2) == int:
            f2 = Fraction(f2).__ensure__int()

        if self.denominator == f2.denominator:
            return Fraction(self.numerator - f2.numerator, self.denominator).simplify()
        else:
            return Fraction(self.numerator * f2.denominator - f2.numerator * self.denominator,
                            self.denominator * f2.denominator).simplify()

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)

        other = other.simplify()
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator).simplify()

    def __truediv__(self, other):
        if type(other) == int:
            return Fraction(self.numerator, self.denominator * other).simplify()
        else:
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator).simplify()

    def __floordiv__(self, other):
        return self.numerator // self.denominator

    def __pow__(self, power):
        if isinstance(power, Fraction):
            if power < 0:
                self.numerator, self.denominator = self.denominator, self.numerator
                power.__mul__(-1)

            self.numerator = self.numerator ** power.numerator
            self.denominator = self.denominator ** power.numerator
            return Fraction(self.numerator, self.denominator).root(power.denominator)
        else:
            return Fraction(self.numerator ** power, self.denominator ** power).__ensure__int()

    def root(self, n=2):
        return Fraction(self.numerator ** (1 / n), self.denominator ** (1 / n)).__ensure__int()

    def __str__(self):
        if self.is_int():
            return str(int(self.numerator // self.denominator))
        else:
            return str(int(self.numerator)) + '/' + str(int(self.denominator))

    def __int__(self):
        if not self.is_int():
            print(Warning('Fraction is not an integer'))

        return round(self.numerator / self.denominator)

    # Replacement for Python 2's lack of __int__() function
    def get_int(self):
        return int(round(self.numerator / self.denominator))

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
        return Fraction(self.numerator, self.denominator).simplify()

    def is_int(self):
        return float(self.numerator / self.denominator) - int(self.numerator / self.denominator) == 0


##### END GATHER #####


def main():
    # f = Fraction(1)
    # f = f / 1002934
    # g = f + 3
    # print(g)
    #
    # print(f)
    print(combination(Fraction(-20, 3), Fraction(6)))
    #
    # print(Fraction(4, 17) ** 2)
    #
    # print(Fraction(9, 16).root(3))
    # n = Fraction(-3, 2)
    # print(factorial(n, n.__sub__(2)))

    # print(gcd(5960797072573, 5960861127242))  # answer: 771743


if __name__ == '__main__':
    main()
