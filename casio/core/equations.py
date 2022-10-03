from math import sqrt, comb, gcd

prohibited_chars = [
    '@',
    '#',
    '$',
    '&',
    ',',
    ';',
    '\\'
]

alphabets = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]


class Equation:
    def __init__(self, equation):
        self.raw = equation
        self.parse()

        print(self.raw)

    def parse(self):
        if type(self.raw) is not str:
            raise TypeError('Type of input is not str')

        for char in prohibited_chars:
            if char in self.raw:
                raise ValueError(f'Input must not contain "{char}"')

        self.raw = self.raw.replace(' ', '')

        for char in alphabets:
            self.raw = self.raw.replace(char, f'*{char}')

        return


def main():
    eq = Equation('x^2 + \\2x + 1')


if __name__ == '__main__':
    main()