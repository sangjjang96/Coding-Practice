import sys
from collections import deque

def bfs():
    q = deque([[0, 0]])
    corner = deque([])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if 0 <= x_ < r and 0 <= y_ < c and not visited[x_][y_]:
                visited[x_][y_] = 1
                
                if maps[x_][y_] == 0:
                    q.append([x_, y_])
                elif maps[x_][y_] == 1:
                    corner.append([x_, y_])
    
    for x, y in corner:
        maps[x][y] = 0
    
    return len(corner)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

r, c = list(map(int, sys.stdin.readline().rstrip().split()))

maps = []

cnt = 0
for i in range(r):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))
    cnt += sum(maps[i])

time = 1
while True:
    visited = [[0]*c for _ in range(r)]
    
    corner_cnt = bfs()
    cnt -= corner_cnt
    
    if cnt == 0:
        print(time, corner_cnt, sep='\n')
        break
    time += 1
