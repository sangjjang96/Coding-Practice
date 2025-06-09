import sys
from collections import deque
import heapq


n, m = list(map(int, sys.stdin.readline().split()))

indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    graph[a].append(b)
    indegree[b] += 1

result = []
q = []

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
    
while q:
    cur = heapq.heappop(q)
    result.append(cur)
    
    for i in graph[cur]:
        indegree[i] -= 1
        
        if indegree[i] == 0:
            heapq.heappush(q, i)

for i in result:
    print(i, end=' ')