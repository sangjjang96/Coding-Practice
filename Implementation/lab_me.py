import sys
from collections import deque
import copy

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, m = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs():
    q = deque([])
    
    maps_tmp = copy.deepcopy(maps)
    
    for i in range(n):
        for j in range(m):
            if maps_tmp[i][j] == 2:
                q.append([i, j])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            while 0 <= x_ < n and 0 <= y_ < m and maps_tmp[x_][y_] == 0:
                maps_tmp[x_][y_] = maps_tmp[x][y]
                q.append([x_, y_])
    
    global ans
    safe = 0
    for i in range(n):
        for j in range(m):
            if maps_tmp[i][j] == 0:
                safe += 1
    
    ans = max(ans, safe)


def make_wall(wall_num):
    if wall_num == 3:
        bfs()
        return
        
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                make_wall(wall_num+1)
                maps[i][j] = 0

ans = 0
make_wall(0)
print(ans)