import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().split()))

indegree = [0]*(n+1)
graphs = [[] for _ in range(n+1)]

for _ in range(m):
    queues = list(map(int, sys.stdin.readline().split()))
        
    for i in range(1, len(queues)-1):
        graphs[queues[i]].append(queues[i+1])
        indegree[queues[i+1]] += 1

def top():
    q = deque()
    ans = []
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        ans.append(now)
        
        for i in graphs[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    if len(ans) != n:
        print(0)
    else:
        for a in ans:
            print(a)
            
top()