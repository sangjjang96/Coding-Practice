import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(sys.stdin.readline())

sectors = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

h_max = 0
h_min = int(1e9)

for sector in sectors:
    h_max = max(h_max, max(sector))
    h_min = min(h_min, min(sector))

def bfs(x, y):
    q = deque([])
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        
        visited[x][y] = 1
        
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < n and visited[x_][y_] == 0 and maps[x_][y_] == 0:
                visited[x_][y_] = 1
                q.append([x_, y_])

ans = 1
for h in range(h_min, h_max+1):
    maps = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if sectors[i][j] <= h:
                maps[i][j] = 1
    
    visited = [[0]*n for _ in range(n)]
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    
    ans = max(ans, cnt)

print(ans)