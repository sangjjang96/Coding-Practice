import sys

t = int(sys.stdin.readline())

def dfs(pos, cnt):
    visited[pos] = 1
    for p in planes[pos]:
        if visited[p] == 0:
            cnt = dfs(p, cnt+1)
    return cnt

for _ in range(t):    
    n, m = list(map(int, sys.stdin.readline().split()))
    
    planes = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = list(map(int, sys.stdin.readline().split()))
        planes[a].append(b)
        planes[b].append(a)

    visited = [0]*(n+1)
    visited[1] = 0
    cnt = dfs(1, 0) 
    print(cnt)