from ..core.fractions import *
from ..core.terms import *


def main():
    terms = []
    expanded_terms = []

    for _ in range(2):
        c = input('c: ')
        p = input('index: ')

        terms.append(Term(coefficient=c, exponent=p))


    ex = int(input('ex: '))

    for i in reversed(list(range(ex + 1))):
        expanded_terms.append(Term(coefficient=Fra, exponent=i))


if __name__ == '__main__':
    main()
