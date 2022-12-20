from math import comb, gcd
from casio.core.terms import *
from casio.core.fractions import *

def find_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)

    return factors


def main():
    print("RRT")
    while True:
        try:
            d = abs(int(input("a0: ")))
            a = abs(int(input("an: ")))

            d_factors = find_factors(d)
            a_factors = find_factors(a)

            possible_roots = []

            for df in d_factors:
                for af in a_factors:
                    nf = Fraction(df, af)
                    rep = False
                    for p in possible_roots:
                        if p == nf:
                            rep = True

                    if not rep:
                        possible_roots.append(nf)

            pr_str = ', '.join([str(x) for x in possible_roots])
            print(f"+-({pr_str})")

            print('-----------')

        except Exception as e:
            print("rrt requires int coefficients")


main()
