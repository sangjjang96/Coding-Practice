T = int(input())

for i in range(T):
    q = 0
    d = 0
    n = 0
    p = 0
    C = int(input())
    
    while C > 0:
        if C >= 25:
            C -= 25
            q += 1
        elif C >= 10:
            C -= 10
            d += 1
        elif C >= 5:
            C -= 5
            n += 1
        else:
            C -= 1
            p += 1

    print(q, d, n, p)