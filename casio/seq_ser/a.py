def d_t(d, n, t):
    if d is not None or len(t) < 2:
        raise Exception()

    for i in range(len(t)):
        for j in range(i+1, len(t)):
            e, f = list(t.keys())[i], t[list(t.keys())[i]]
            g, h = list(t.keys())[j], t[list(t.keys())[j]]
            
            e = int(e)
            g = int(g)
            
            if (h - f) / (g - e) != d and d != None:
                raise Exception('na')
            else:
                d = (h - f) / (g - e)
                
    if int(d) == d:
        d = int(d)
        
    return d

def main():
    d = input('d: ')
    n = input('n: ')
    
    try:
        if d != '':
            d = int(d)
        else:
            d = None
        
        if n != '':
            n = int(n)
        else:
            n = None
            
    except Exception:
        exit(0)
    
    t = {}
    
    while True:
        a = input()
        if a == ',':
            break
        elif ',' in a:
            try:
                an = int(a.split(',')[0])
                a = int(a.split(',')[1])
                assert str(an) not in t
                t[str(an)] = a
            except Exception as e:
                print('e')
                continue
        else:
            try:
                assert 'n' not in t
                a = int(a)
                t['n'] = a
            except Exception as e:
                print('e')
                continue
    
    
    print(f'd:{d_t(d, n, t)}')
    

if __name__ == '__main__':
    main()