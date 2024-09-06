import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, m = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(x, y):
    maps_tmp = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    
    q = deque([])
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < m and maps[x_][y_] == 1 and visited[x_][y_] != 1:
                q.append([x_, y_])
                visited[x_][y_] = 1
                maps_tmp[x_][y_] = maps_tmp[x][y] + 1
    
    return maps_tmp


for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            start = [i, j]
            answer = bfs(i, j)
            break
    
around = []    
for i in range(4):
    x_ = start[0] + dx[i]
    y_ = start[1] + dy[i]
    around.append([x_, y_])

for i in range(n):
    for j in range(m):
        if answer[i][j] == 0:
            if [i, j] == start or [i, j] in around:
                print(answer[i][j], end=' ')
            else:
                if maps[i][j] == 1:
                    print(-1, end=' ')
                else:
                    print(0, end=' ')
        else:
            print(answer[i][j], end=' ')
    print()