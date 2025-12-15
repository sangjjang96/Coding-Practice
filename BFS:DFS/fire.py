import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
curT = 0


r, c = list(map(int, sys.stdin.readline().split()))

maps = []

for _ in range(r):
    tmp = []
    txt = sys.stdin.readline().rstrip()
    
    for t in txt:
        tmp.append(t)
    
    maps.append(tmp)
        
q = deque([])
fires = deque([])

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'J':
            q.append([i, j, 0])
        elif maps[i][j] == 'F':
            fires.append([i, j, 0])

while q:
    curT += 1
    
    while q and q[0][2] < curT:
        x, y, t = q.popleft()
        
        if (x == 0 or x == r-1 or y == 0 or y == c-1) and maps[x][y] == 'J':
            print(t+1)
            exit()
        
        for k in range(4):
            x_, y_ = x + dx[k], y + dy[k]
            
            if 0 <= x_ < r and 0 <= y_ < c:
                if maps[x_][y_] == '.':
                    maps[x_][y_] = 'J'
                    q.append([x_, y_, t+1])
    
    while fires and fires[0][2] < curT:
        x, y, t = fires.popleft()
        
        for k in range(4):
            x_, y_ = x + dx[k], y + dy[k]
            
            if 0 <= x_ < r and 0 <= y_ < c:
                if maps[x_][y_] == '.' or maps[x_][y_] == 'J':
                    maps[x_][y_] = 'F'
                    fires.append([x_, y_, t+1])

print('IMPOSSIBLE')