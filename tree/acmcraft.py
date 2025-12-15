import sys
from collections import deque

T = int(sys.stdin.readline())

res = []
for _ in range(T):
    ans = 0
    no_seq = False
    
    n, k = list(map(int, sys.stdin.readline().split()))
    
    times = [0] + list(map(int, sys.stdin.readline().split()))
    
    graphs = [[] for _ in range(n+1)]
    
    indegree = [0]*(n+1)
    tech = [[] for _ in range(n+1)]
    
    for _ in range(k):
        a, b = list(map(int, sys.stdin.readline().split()))
        
        graphs[a].append(b)
        indegree[b] += 1
    
    w = int(sys.stdin.readline())
    
    dp = [0]*(n+1)
    def topological_sort():
        q = deque([])
        
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = times[i]
        
        while q:
            now = q.popleft()
            
            for i in graphs[now]:
                indegree[i] -= 1
                dp[i] = max(dp[i], dp[now] + times[i])
                
                if indegree[i] == 0:
                    q.append(i)
                    
    topological_sort()
    res.append(dp[w])

for r in res:
    print(r)