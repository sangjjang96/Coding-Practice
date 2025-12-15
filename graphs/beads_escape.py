import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = list(map(int, sys.stdin.readline().split()))

boards = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if boards[i][j] == 'R':
            rx, ry = i, j
        elif boards[i][j] == 'B':
            bx, by = i, j
            
def move(x, y, dx, dy):
    cnt = 0
    
    while boards[x+dx][y+dy] != '#' and boards[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    
    return x, y, cnt
        
visited = []
    
def bfs():
    q = deque([])
    q.append([rx, ry, bx, by, 1])
    
    visited.append([rx, ry, bx, by])
    
    while q:
        red_x, red_y, blue_x, blue_y, count = q.popleft()
        
        if count > 10:
            break
        
        for i in range(4):
            red_x_, red_y_, r_cnt = move(red_x, red_y, dx[i], dy[i])
            blue_x_, blue_y_, b_cnt = move(blue_x, blue_y, dx[i], dy[i])
            
            if boards[blue_x_][blue_y_] == 'O':
                continue
            
            if boards[red_x_][red_y_] == 'O':
                if count <= 10:
                    print(1)
                else:
                    print(0)
                return
            
            if red_x_ == blue_x_ and red_y_ == blue_y_:
                if r_cnt > b_cnt:
                    red_x_ -= dx[i]
                    red_y_ -= dy[i]
                else:
                    blue_x_ -= dx[i]
                    blue_y_ -= dy[i]
            
            if [red_x_, red_y_, blue_x_, blue_y_] not in visited:
                visited.append([red_x_, red_y_, blue_x_, blue_y_])
                q.append([red_x_, red_y_, blue_x_, blue_y_, count+1])
        
    print(0)

bfs()
