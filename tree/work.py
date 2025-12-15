import sys
from collections import deque

n = int(sys.stdin.readline())

indegree = [[] for _ in range(n+1)]
graphs = [[] for _ in range(n+1)]
times = [0]*(n+1)

total_time = 0

for i in range(1, n+1):
    inp = list(map(int, sys.stdin.readline().split()))
    
    time = inp[0]
    total_time += time
    
    times[i] = time
    
    num = inp[1]
    
    indegree[i] = inp[2:]
    
    for k in inp[2:]:
        graphs[k].append(i)

q = deque()

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

t = 0
while q:
    l = len(q)
    
    for _ in range(l):
        work_idx = q.popleft()
        
        times[work_idx] -= 1
        
        if times[work_idx] == 0:
            for g in graphs[work_idx]:
                indegree[g].remove(work_idx)
                
                if not indegree[g]:
                    q.append(g)
        else:
            q.append(work_idx)
            
    t += 1
    
print(t)
    