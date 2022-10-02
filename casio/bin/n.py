from math import comb

def gather_input():
    a1 = int(input('a1'))
    b1 = int(input('b1'))
    p1 = int(input('p1'))

    a2 = int(input('a2'))
    b2 = int(input('b2'))
    p2 = int(input('p2'))

    t = int(input('target'))

    return a1, b1, p1, a2, b2, p2, t

def coefficient(a1, b1, p1, a2, b2, p2, v):
    i, j = v
    c = comb(p1, i)


def main():
    try:
        a1, b1, p1, a2, b2, p2, t = gather_input()
    except ValueError as e:
        print('err')
        main()

    p1l = range(p1)
    p2l = range(p2)

    valid = []

    for i in p1l:
        for j in p2l:
            if i + j == t:
                valid.append((i, j))


    for v in valid:
        coefficient(a1, b1, a2, b2, v)

    pass

if __name__ == '__main__':
    main()