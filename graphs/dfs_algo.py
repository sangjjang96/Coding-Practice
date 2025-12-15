import sys

n, m, r = list(map(int, sys.stdin.readline().split()))

graphs = [[] for _ in range(n+1)]

edges = []
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    edges.append([a, b])

edges.sort()

for edge in edges:
    a, b = edge
    
    graphs[a].append(b)
    graphs[b].append(a)
    
order = []

visited = [0]*(n+1)
def dfs(s):
    global visited, order
    
    order.append(s)
    visited[s] = 1
    
    for x in graphs[s]:
        if not visited[x]:
            dfs(x)

dfs(r)

for i in range(1, n+1):
    if visited[i] == 1:
        print(i)
    else:
        print(0)