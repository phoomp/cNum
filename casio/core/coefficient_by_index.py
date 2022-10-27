from math import comb, gcd
from casio.core.terms import *
from casio.core.fractions import *

##### BEGIN GATHER #####


def solve_given_index(t1, t2, power, index):
    assert type(t1) == Term and type(t2) == Term
    assert type(index) == int

    print(t1)
    print(t2)
    print(power)
    print(index)

    coefficient1 = Fraction(combination(power, Fraction(index)))
    coefficient2 = (t1.coefficient.__pow__(power - index))  # Do this to avoid unsupported *=
    coefficient3 = (t2.coefficient.__pow__(index))

    print(coefficient1)
    print(coefficient2)
    coefficient = coefficient1.__mul__(coefficient2)
    coefficient = coefficient.__mul__(coefficient3)

    degree = (t1.exponent.__mul__(power - index)).__add__(t2.exponent.__mul__(index))

    return Term(coefficient=coefficient, exponent=degree)


def main():
    try:
        t1c = Fraction(input('t1c: '))
        t1e = Fraction(input('t1e: '))
        t2c = Fraction(input('t2c: '))
        t2e = Fraction(input('t2e: '))
        p = Fraction(input('p: '))
        t = int(input('t idx: '))

    except Exception as e:
        print('err')
        main()

    t1 = Term(t1c, exponent=t1e)
    t2 = Term(t2c, exponent=t2e)

    res = solve_given_index(t1, t2, p, t - 1)  # 0-indexing

    # Python 3 only
    # print(f'c: {res.coefficient}')
    # print(f'ex: {res.exponent}')

    print('c: ' + str(res.coefficient))
    print('ex: ' + str(res.exponent))


# Python 3 only
# if __name__ == '__main__':
#     main()

# Python 2
while True:
    main()

##### END GATHER #####