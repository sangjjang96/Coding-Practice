import sys
import heapq

n, m = list(map(int, sys.stdin.readline().split()))

distances = [[int(1e9)]*(n+1) for _ in range(n+1)]
ans = [['-']*(n+1) for _ in range(n+1)]
    
for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    distances[a][b] = distances[b][a] = c
    ans[a][b] = str(b)
    ans[b][a] = str(a)
    
def folyd(n, dists, a):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    a[i][j] = a[i][k]
    
    return a
    

ans = folyd(n, distances, ans)

for a in ans[1:]:
    print(*a[1:])

