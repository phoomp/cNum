from ..core.fractions import *
from ..core.terms import *


def main():
    try:
        t1c = int(input('t1c: '))
        t1e = int(input('t1e: '))
        t2c = int(input('t2c: '))
        t2e = int(input('t2e: '))
        p = int(input())

        t1 = Term(t1c, t1e)
        t2 = Term(t2c, t2e)

    except Exception as e:
        print('err')
        main()

    for i in range(


if __name__ == '__main__':
    main()
