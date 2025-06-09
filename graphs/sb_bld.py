import sys
from collections import deque

def bfs():
    q = deque([])
    visited = [[[0]*c for _ in range(r)] for _ in range(l)]
    
    q.append([l_start, x_start, y_start, [[l_start, x_start, y_start]]])
    
    while q:
        lvl, x, y, path = q.popleft()
        
        if [lvl, x, y] == [l_end, x_end, y_end]:
            return len(path), path
        
        visited[lvl][x][y] = 1
        
        for d in range(6):
            lvl_, x_, y_ = lvl + dl[d], x + dx[d], y + dy[d]
            
            if 0 <= lvl_ < l and 0 <= x_ < r and 0 <= y_ < c and maps[lvl_][x_][y_] == 0 and not visited[lvl_][x_][y_]:
                visited[lvl_][x_][y_] = 1
                q.append([lvl_, x_, y_, path + [[lvl_, x_, y_]]])

    return -1, []

dl = [0, 0, 0, 0, 1, -1]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]

l_start, x_start, y_start = -1, -1, -1
l_end, x_end, y_end = -1, -1, -1

while True:
    l, r, c = map(int, input().split())
    
    if [l, r, c] == [0, 0, 0]:
        break

    maps = [[[0]*c for _ in range(r)] for _ in range(l)]


    for k in range(l):
        m = [list(map(str, input())) for _ in range(r)]
        _ = input()
        
        for i in range(r):
            for j in range(c):
                if m[i][j] == 'S':
                    m[i][j] = 0
                    l_start = k
                    x_start = i
                    y_start = j
                elif m[i][j] == 'E':
                    m[i][j] = 0
                    l_end = k
                    x_end = i
                    y_end = j
                elif m[i][j] == '.':
                    m[i][j] = 0
                elif m[i][j] == '#':
                    m[i][j] = 1
        
        maps[k] = m

    ans, p = bfs()

    if ans == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {ans-1} minute(s).')
