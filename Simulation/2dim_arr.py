import sys

N, M = list(map(int, sys.stdin.readline().split()))

arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

K = int(sys.stdin.readline())

for k in range(K):
    i, j, x, y = list(map(int, sys.stdin.readline().split()))
    
    sum = 0
    for c in range(i-1, x):
        for r in range(j-1, y):
            sum += arr[c][r]
    
    print(sum)