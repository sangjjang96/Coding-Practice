import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

size, low, high = list(map(int, sys.stdin.readline().split()))

land = []
q = deque([])

for _ in range(size):
    land.append(list(map(int, sys.stdin.readline().split())))

def bfs(x, y):
    q = deque([])
    q.append([x, y])
    visited[x][y] = True
    union = [[x, y]]
    
    while q:
        x, y= q.popleft()
        
        for i in range(4):
            move = True
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < size and 0 <= new_y < size and not visited[new_x][new_y]:
                if low <= abs(land[x][y] - land[new_x][new_y]) <= high:
                    visited[new_x][new_y] = True
                    q.append([new_x, new_y])
                    union.append([new_x, new_y])
    
    return union

day = 0
while True:
    visited = [[False]*size for _ in range(size)]
    move = False
    
    for i in range(size):          
        for j in range(size):
            if not visited[i][j]:
                union = bfs(i, j)
                
                if len(union) > 1:
                    move = True
                    summation = sum(land[i][j] for i, j in union) // len(union)

                    for i, j in union:
                        land[i][j] = summation
    
    if not move:
        break
    day += 1

print(day)