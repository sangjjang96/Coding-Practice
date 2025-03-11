import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, m = list(map(int, sys.stdin.readline().split()))

maps = []
maps_cnt = [[0]*m for _ in range(n)]

cheese_num = 0

for i in range(n):
    info = list(map(int, sys.stdin.readline().split()))
    maps.append(info)
    cheese_num += sum(info)


def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] >= 1: 
                    maps[nx][ny] += 1
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = True

def count():
    melted = 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] >= 3:
                maps[i][j] = 0
                melted += 1
            elif maps[i][j] >= 2:
                maps[i][j] = 1
    return melted

time = 0
while True:
    bfs()
    melted = count()
    
    if melted:
        time += 1
    else:
        print(time)
        break