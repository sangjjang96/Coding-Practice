import sys
from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs():
    visited = [[0]*w for _ in range(h)]
    while q:
        x, y = q.popleft()
        
        maps[x][y] = 11
        visited[x][y] = 1
        
        for i in range(8):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if 0 <= x_ < h and 0 <= y_ < w and maps[x_][y_] == 1 and not visited[x_][y_]:
                visited[x_][y_] = 1
                q.append([x_, y_])

while True:
    w, h = list(map(int, sys.stdin.readline().split()))
    
    if [w, h] == [0, 0]:
        break
    
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    q = deque([])
    ans = 0
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                q.append([i, j])
                bfs()
                ans += 1
    
    print(ans)