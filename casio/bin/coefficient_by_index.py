from math import comb, gcd
from ..core.terms import *
from ..core.fractions import *

##### BEGIN GATHER #####

def solve_given_index(t1, t2, power, index):
    assert type(t1) == Term and type(t2) == Term
    assert int(index) == index

    coefficient = combination(Fraction(power), Fraction(index))
    coefficient *= t1.coefficient ** (power - index)
    coefficient *= t2.coefficient ** index

    degree = t1.exponent * (power - index) + t2.exponent * index

    return Term(coefficient=coefficient, exponent=degree)


def main():
    try:
        t1c = Fraction(input('t1c: '))
        t1e = Fraction(input('t1e: '))
        t2c = Fraction(input('t2c: '))
        t2e = Fraction(input('t2e: '))
        p = Fraction(input('p: '))
        t = Fraction(input('t idx: '))

    except TypeError as e:
        print('err')
        main()

    t1 = Term(t1c, exponent=t1e)
    t2 = Term(t2c, exponent=t2e)

    res = solve_given_index(t1, t2, p, t)
    print(f'c: {res.coefficient}')
    print(f'ex: {res.exponent}')


if __name__ == '__main__':
    main()

##### END GATHER #####