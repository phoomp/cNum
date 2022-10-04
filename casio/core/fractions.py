# Lightweight Fractions Library for Python
# Created by Phoom Punpeng
# 2022-10-02

##### BEGIN GATHER #####

# GCD Function, for Python 2
def gcd(a, b):
    # Find minimum of a and b
    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    # Return the gcd of a and b
    return int(result)


def similar(f1, f2):
    if type(f1) != Fraction or type(f2) != Fraction:
        raise TypeError('Arguments must be of type Fraction')


def factorial(n, limit=None):
    if (limit is not None and n <= limit) or (limit is None and n < 1):
        return 1
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
        if self.numerator <= 0 or self.denominator < 0:
            return self
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
        if type(power) == Fraction:
            if power < 0:
                self.numerator, self.denominator = self.denominator, self.numerator
                power *= -1

            self.numerator = self.numerator ** power.numerator
            self.denominator = self.denominator ** power.numerator

            return Fraction(self.numerator, self.denominator).root(power.denominator)
        else:
            return Fraction(self.numerator ** power, self.denominator ** power).__ensure__int()

    def root(self, n=2):
        return Fraction(self.numerator ** (1 / n), self.denominator ** (1 / n)).__ensure__int()

    def __str__(self):
        if self.is_int():
            return str(self.numerator // self.denominator)
        else:
            return str(self.numerator) + '/' + str(self.denominator)

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
        return self.simplify()

    def is_int(self):
        return float(self.numerator / self.denominator) - int(self.numerator / self.denominator) == 0

##### END GATHER #####


def main():
    # print(combination(Fraction(1, 4), Fraction(6, 2)))

    print(Fraction(4, 16) ** 2)

    # print(Fraction(9, 16).root(2))


if __name__ == '__main__':
    main()
