import sys
from collections import deque

n = int(input())

indegree = [0]*(n+1)

graphs = [[] for _ in range(n+1)]

dp = [0]*(n+1)
cost = [0]*(n+1)

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))[:-1]
    
    cost[i+1] = tmp[0]
    for j in tmp[1:]:
        graphs[j].append(i+1)
        indegree[i+1] += 1

q = deque([])

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)
        dp[i] = cost[i]

while q:
    n = q.popleft()
    
    for i in graphs[n]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[n] + cost[i])
        
        if not indegree[i]:
            q.append(i)

for d in dp[1:]:
    print(d)