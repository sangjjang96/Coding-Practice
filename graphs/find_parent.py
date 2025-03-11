import sys
from collections import deque

n = int(input())

nodes = [[0] for _ in range(n+1)]

ans = [0]*(n+1)

for _ in range(n-1):
    f, t = list(map(int, sys.stdin.readline().split()))
    
    nodes[f].append(t)
    nodes[t].append(f)

ans[1] = 0
q = deque()
q.append(1)

while q:
    cur = q.popleft()
    for n in nodes[cur]:
        if ans[n] == 0:
            ans[n] = cur
            q.append(n)

for a in ans[2:]:
    print(a)