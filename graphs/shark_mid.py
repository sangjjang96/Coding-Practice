import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x_in, y_in, idx):
    q = deque([])
    q.append([x_in, y_in])
    
    blo_cnt, rain_cnt = 1, 0
    blo_path, rain_path = [[x_in, y_in]], []
    
    while q:
        x, y = q.popleft()
                
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < n and not visited[x_][y_] and grids[x_][y_] == idx:
                visited[x_][y_] = 1
                q.append([x_, y_])
                blo_cnt += 1
                blo_path.append([x_, y_])
            
            elif 0 <= x_ < n and 0 <= y_ < n and not visited[x_][y_] and grids[x_][y_] == 0:
                visited[x_][y_] = 1
                q.append([x_, y_])
                blo_cnt += 1
                rain_cnt += 1
                rain_path.append([x_, y_])
    
    for x, y in rain_path:
        visited[x][y] = 0
    
    return [blo_cnt, rain_cnt, blo_path + rain_path]

def remove(blo):
    for x, y in blo:
        grids[x][y] = -2
    
def gravity(g):
    for i in range(n-2, -1, -1):
        for j in range(n):
            if g[i][j] > -1:
                r = i
                while True:
                    if 0 <= r+1 < n and g[r+1][j] == -2:
                        g[r+1][j] = g[r][j]
                        g[r][j] = -2
                        r += 1
                    else:
                        break

def rot(g):
    new_g = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_g[n-1-j][i] = g[i][j]
    
    return new_g
    
n, m = list(map(int, sys.stdin.readline().split()))

grids = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

score = 0

while True:
    visited = [[0]*n for _ in range(n)]
    blocks = []
    
    for i in range(n):
        for j in range(n):
            if grids[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_info = bfs(i, j, grids[i][j])
                
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)
    
    if not blocks:
        break
    
    remove(blocks[0][2])
    score += blocks[0][0]**2
    
    gravity(grids)
    
    grids = rot(grids)
    
    gravity(grids)

print(score)