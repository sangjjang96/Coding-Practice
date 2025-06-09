import sys

n = int(input())
k = int(input())

arr = [[0]*n for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i-1][j-1] = i*j

for a in arr:
    print(a)

print((k//n + 1) * (k%n + 1))