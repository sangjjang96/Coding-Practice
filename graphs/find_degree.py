import sys
from collections import deque

n = int(sys.stdin.readline())

start, end = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

child = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    child[a].append(b)
    parent[b].append(a)

visited_child = [0 for _ in range(n+1)]
visited_parent = [0 for _ in range(n+1)]

ans = -1

def dfs(start, end, idx):
    global ans
    
    if start == end:
        ans = idx
    
    for c in child[start]:
        if not visited_child[c]:
            visited_child[c] = 1
            dfs(c, end, idx+1)
        
    for p in parent[start]:
        if not visited_parent[p]:
            visited_parent[p] = 1
            dfs(p, end, idx+1)
    

dfs(start, end, 0)
print(ans)