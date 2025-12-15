import sys

n, m = list(map(int, sys.stdin.readline().split()))

arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = arr[i-1][j] + 1

ans = 0

for i in range(n):
    a = arr[i]
    a.sort(reverse=True)
    
    for j in range(m):
        size = (j+1) * a[j]
        ans = size if size > ans else ans

print(ans)