import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().split()))

indegree = [0] * (n+1)
graphs = [[] for _ in range(n+1)]
ans = [0]*(n+1)

for _ in range(m):
    prv, nxt = list(map(int, sys.stdin.readline().split()))
    
    graphs[prv].append(nxt)
    indegree[nxt] += 1

l = deque([])
for i in range(1, n+1):
    if indegree[i] == 0:
      l.append((i, 1))

while l:
      cur, sem = l.popleft()
      
      ans[cur] = sem
      
      for graph in graphs[cur]:
          indegree[graph] -= 1
          
          if indegree[graph] == 0:
              l.append((graph, sem+1))

print(*ans[1:])