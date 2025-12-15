import sys
from collections import deque
from itertools import *

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = list(map(int, sys.stdin.readline().split()))

status = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
avail = []
walls = []

ans = int(1e9)
def bfs(virus, walls):
    global ans
    
    visited = [[0]*n for _ in range(n)]
    times = [[0]*n for _ in range(n)]
    q = deque(virus)
    
    for v in virus:
        x, y = v
        visited[x][y] = 1
    
    for w in walls:
        x, y = w
        times[x][y] = -1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < n and status[x_][y_] != 1 and not visited[x_][y_]:
                visited[x_][y_] = 1
                times[x_][y_] = times[x][y] + 1
                q.append((x_, y_))
    
    zero_cnt = 0
    minus_cnt = 0
    for t in times:
        zero_cnt += t.count(0)
        minus_cnt += t.count(-1)

    if zero_cnt == len(virus) and minus_cnt == len(walls):
        t_max = 0
        for t in times:
            t_max = max(t_max, max(t))
            
        ans = min(ans, t_max)
    else:
        ans = min(ans, int(1e9))
        

for i in range(n):
    for j in range(n):
        if status[i][j] == 2:
            avail.append((i, j))
        if status[i][j] == 1:
            walls.append((i, j))

for v in combinations(avail, m):
    bfs(list(v), walls)

if ans == int(1e9):
    print(-1)
else:
    print(ans)
    
    