T = int(input())

l = [0] * 101
l[1] = 1
l[2] = 1
l[3] = 1
l[4] = 2
l[5] = 2

for i in range(T):
    N = int(input())

    if N >= 6:
        for i in range(6, N+1):
            l[i] = l[i-1] + l[i-5]
        
        print(l[N])
    else:
        print(l[N])
