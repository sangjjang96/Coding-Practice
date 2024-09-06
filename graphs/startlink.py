import sys
from collections import deque


F, S, G, U, D = list(map(int, sys.stdin.readline().split()))

visited = [0 for _ in range(F+1)]
count = [0 for _ in range(F+1)]

def bfs():
    q = deque([S])
    visited[S] = 1

    while q:
        now = q.popleft()
        
        if now == G:
            return count[G]

        for i in [now+U, now-D]:
            if 1 <= i <= F and not visited[i]:
                visited[i] = 1
                count[i] = count[now] + 1
                q.append(i)
    if count[G] == 0:
        return 'use the stairs'

print(bfs())