import sys
from collections import deque

ans = 0
cands = []
n, m = list(map(int, sys.stdin.readline().split()))

relations = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    relations[b].append(a)

def bfs(start):
    visited = [0 for _ in range(n+1)]
    visited[start] = True
    
    q = deque([start])
    
    while q:
        s = q.popleft()
        
        for i in relations[s]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    
    return sum(visited)

ans = []
v_max = 0

for i in range(1, n+1):
    v_cur = bfs(i)
    
    if v_max < v_cur:
        ans = [i]
        v_max = v_cur
    elif v_max == v_cur:
        ans.append(i)

print(*ans)