import sys
from collections import deque

n, m, r = list(map(int, sys.stdin.readline().split()))

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = [[0]*m for _ in range(n)]

q = deque()

for i in range(min(n, m) // 2):
    q.clear()
    
    q.extend(arr[i][i:m-i])
    q.extend(row[m-i-1] for row in arr[i+1:n-i-1])
    q.extend(arr[n-i-1][i:m-i][::-1])
    q.extend([row[i] for row in arr[i+1:n-i-1]][::-1])
    
    q.rotate(-r)
    
    for j in range(i, m-i):
        ans[i][j] = q.popleft()
    for j in range(i+1, n-i-1):
        ans[j][m-i-1] = q.popleft()
    for j in range(m-i-1, i-1, -1):
        ans[n-i-1][j] = q.popleft()
    for j in range(n-i-2, i, -1):
        ans[j][i] = q.popleft()

for a in ans:
    print(a)