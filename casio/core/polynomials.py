from casio.core.fractions import *
from casio.core.terms import *


class Polynomial:
    def __init__(self, terms):
        assert isinstance(terms, dict)
        self.terms = terms

    def __check_valid_type__(self, other):
        assert isinstance(other, Polynomial) or isinstance(other, int)

    def __add__(self, other):
        self.__check_valid_type__(other)
        new_terms = {}

        for a, b in self.terms.items():
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
                new_terms[a] += b

        for c, d in other.terms.items():
            if c not in new_terms:
                new_terms[c] = d
            else:
                new_terms[c] += d

        return Polynomial(new_terms)


    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __pow__(self, power):
        pass

    def __str__(self):
        pass