from casio.core.fractions import *

##### BEGIN GATHER #####

def main():
    try:
        # # Python 2
        # n = Fraction(raw_input('n: '))
        # r = int(raw_input('r: '))

        # Python 3
        n = Fraction(input('n: '))
        r = int(input('r: '))

        if r < 0:
            raise ValueError()

    except Exception:
        print('err')
        main()

    print(combination(n, r))
    main()

# if __name__ == '__main__':  # For Python 3 only
#     main()


main()

##### END GATHER #####
