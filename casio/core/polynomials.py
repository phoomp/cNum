from casio.core.fractions import *
from casio.core.terms import *


class Polynomial:
    def __init__(self, terms):
        assert isinstance(terms, list)
        self.terms = terms

    def __check_valid_type__(self, other):
        assert isinstance(other, Polynomial) or isinstance(other, int)

    def __add__(self, other):
        self.__check_valid_type__(other)
        new_terms = {}

        for item in self.terms:
            for a, b in item.items():
               if a not in new_terms:
                   new_terms[a] = b
               else:
                   new_terms[a] += b

               for c, d in other.terms.items():
                   if c not in new_terms:
                        new_terms[c] = d
                   else:
                        new_terms[c] += d

        return Polynomial(new_terms)

    def __sub__(self, other):
        self.__check_valid_type__(other)
        new_terms = {}

        for a, b in self.terms.items():
            if a not in new_terms:
                new_terms[a] = b
            else:
                new_terms[a] -= b

        for c, d in other.terms.items():
            if c not in new_terms:
                new_terms[c] = d
            else:
                new_terms[c] -= d

        return Polynomial(new_terms)


    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __pow__(self, power):
        pass

    def __str__(self):
        pass


def main():
    term_1 = Term(Fraction(1, 3), 5)
    term_2 = Term(Fraction(2, 9), 2)
    term_3 = Term(Fraction(1, 9))
    term_4 = Term(Fraction(2, 3), 5)

    poly_1 = Polynomial([term_1, term_2, term_3])
    poly_2 = Polynomial([term_4])

    print(poly_1 + poly_2)


if __name__ == '__main__':
    main()