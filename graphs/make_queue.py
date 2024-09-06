import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))

degree = [0]*(N+1)
compare = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    compare[a].append(b)
    degree[b] += 1

def top_sort():
    result = []
    q = deque()
    
    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        result.append(node)
        
        for next in compare[node]:
            degree[next] -= 1
            
            if degree[next] == 0:
                q.append(next)
                
    for i in result:
        print(i, end=' ')
    
top_sort()