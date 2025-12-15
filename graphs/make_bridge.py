import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(sys.stdin.readline())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

continents = [[0]*n for _ in range(n)]

def make_continent(x, y, idx):
    q = deque([])
    visited = [[0]*n for _ in range(n)]
    
    q.append([x, y])
    visited[x][y] = 1
    continents[x][y] = idx
    
    while q:
        x_cur, y_cur = q.popleft()
        
        for i in range(4):
            x_new, y_new = x_cur + dx[i], y_cur + dy[i]
            
            if 0 <= x_new < n and 0 <= y_new < n and not visited[x_new][y_new] and maps[x_new][y_new] == 1:
                visited[x_new][y_new] = 1
                continents[x_new][y_new] = idx
                q.append([x_new, y_new])


def find_bridge(start_idx):
    q = deque([])
    distances = [[-1]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if continents[i][j] == start_idx:
                q.append([i, j])
                distances[i][j] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < n:
                if continents[x_][y_] != start_idx and continents[x_][y_]:
                    return distances[x][y]
                if continents[x_][y_] == 0 and distances[x_][y_] == -1:
                    distances[x_][y_] = distances[x][y] + 1
                    q.append([x_, y_])

idx = 11
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and continents[i][j] == 0:
            make_continent(i, j, idx)
            idx += 1

ans = int(1e9)
for i in range(11, idx):
    ans = min(ans, find_bridge(i))

print(ans)