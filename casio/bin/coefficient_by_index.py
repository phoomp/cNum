from math import comb, gcd

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
    t1 = Term(7, exponent=3)
    t2 = Term(4, exponent=-1)

    res = solve_given_index(t1, t2, 9, 9)
    print(res.coefficient)
    print(res.exponent)


if __name__ == '__main__':
    main()

##### END GATHER #####