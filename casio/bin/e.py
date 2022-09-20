from math import comb

def main():
    n = input('n: ')
    
    for i in n:
        a = int(input(f'a{i}: '))
        b = int(input(f'b{i}x: '))
        p = int(input(f'p{i}: '))
        
        t = 0
        an = ''
        while t <= p:
            c = comb(p, t) * pow(a, p - t) * pow(b, t)
            print(f'{c}x^{t}')
            t += 1
        

if __name__ == '__main__':
    main()