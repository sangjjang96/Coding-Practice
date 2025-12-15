import sys
from collections import deque

k = int(sys.stdin.readline())

def odd_even(x):
    return 1 if x % 2 == 0 else -1
    
def bfs(x):
    q = deque([])
    
    lvl = 0
    
    q.append((x, lvl+1))
    visited[x] = odd_even(lvl)
    
    while q:
        x_, lvl_ = q.popleft()

        for i in graph[x_]:
            if not visited[i]:
                q.append((i, lvl_+1))
                visited[i] = odd_even(lvl_)
            
            elif visited[i] == odd_even(lvl_):
                continue
            
            elif visited[i] != odd_even(lvl_):
                return False
    
    return True


result = []
for _ in range(k):
    v, e = list(map(int, sys.stdin.readline().split()))
    
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        a, b = list(map(int, sys.stdin.readline().split()))
        
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0]*(v+1)
    
    graph_l = []
    for i in range(1, v+1):
        if not visited[i]:
            graph_l.append(bfs(i))
    
    if all(graph_l):
        result.append('YES')
    else:
        result.append('NO')
    

for r in result:
    print(r)