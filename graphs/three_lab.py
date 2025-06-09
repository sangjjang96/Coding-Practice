import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = list(map(int, sys.stdin.readline().split()))

laboratory = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = int(1e9)

def check(visited):
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and laboratory[i][j] == 0:
                return False
    
    return True

def bfs(q):
    time = 1
    
    visited = [[0]*n for _ in range(n)]
    for x, y, t in q:
        visited[x][y] = 1
    
    while q:
        x, y, t = q.popleft()
        
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
        
            if 0 <= x_ < n and 0 <= y_ < n and not visited[x_][y_]:
                if laboratory[x_][y_] == 0:
                    time = max(t+1, time)
                    q.append([x_, y_, t+1])
                    visited[x_][y_] = t+1
                if laboratory[x_][y_] == 2:
                    q.append([x_, y_, t+1])
                    visited[x_][y_] = t+1
        
    if check(visited):
        return max(time-1, 0)
    else:
        return -1

virus_pos = []

for i in range(n):
    for j in range(n):
        if laboratory[i][j] == 2:
            virus_pos.append([i, j, 1])

from itertools import combinations

for c in combinations(virus_pos, m):
    result = bfs(deque(c))
    ans = min(ans, result) if result != -1 else ans
    

print(ans if ans != int(1e9) else -1)