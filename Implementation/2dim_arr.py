import sys

N, M = list(map(int, sys.stdin.readline().split()))

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

K = int(sys.stdin.readline())

for k in range(K):
    i, j, x, y = list(map(int, sys.stdin.readline().split()))
    
    cum = 0
    for r in range(i-1, x):
        for c in range(j-1, y):
            cum += arr[r][c]
    
    print(cum)