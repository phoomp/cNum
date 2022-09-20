from math import comb, factorial
from fractions import Fraction

def solve(a1, b1, c1, a2, b2, c2):
    # [a1, b1] = c1
    # [a2, b2] = c2
    
    m1 = a2 / a1
    
    a1 *= m1
    b1 *= m1
    c1 *= m1
    
    bp = b2 - b1
    cp = c2 - c1
    
    b = cp / bp
    a = (c1 - (b1 * b)) / a1

    if int(a) - a < 1e-5:
        a = round(a)
    
    if int(b) - b < 1e-5:
        b = round(b)
    
    return a, b


def cm(a, b):
    s = 1
    n = a
    while n >= a - b + 1:
        s *= n
        n -= 1
        
    return Fraction(s / int(factorial(b)))


def main():
    print(cm(-5, 2))
    print(solve(20, 10, 350, 17, 22, 500))
    while True:
        a = input('a: ')
        pa = int(input('ax^?: '))
        
        b = input('b: ')
        pb = int(input('bx^?: '))
        
        p = int(input('p: '))
        t = int(input('t: '))
        
        n, m = solve(pa, pb, t, 1, 1, p)
        
        try:
            a = Fraction(a).limit_denominator()
            b = Fraction(b).limit_denominator()
            # n = Fraction(n).limit_denominator()
            m = Fraction(m).limit_denominator()
            
        except Exception as e:
            print(e)
            break
        
        c = cm(p, n) * pow(a, n) * pow(b, m)
        
        print(c)
        
if __name__ == '__main__':
    main()