from itertools import *

N, K = list(map(int, input().split()))
WV = [[0, 0]]
bags = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N):
    WV.append(list(map(int, input().split())))
    

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = WV[i][0]
        value = WV[i][1]
        
        if j < weight:
            bags[i][j] = bags[i-1][j]
        else:
            bags[i][j] = max(value + bags[i-1][j-weight], bags[i-1][j])
            
print(bags[N][K])