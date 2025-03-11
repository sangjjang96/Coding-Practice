import sys
import copy
from collections import deque

m, n, h = list(map(int, sys.stdin.readline().split()))

boxes = []

# w s n e u d
dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 0, 0, 1, 0, 0]
dy = [0, -1, 1, 0, 0, 0]

total = 0

for _ in range(h):
    box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    for bo in box:
        for b in bo:
            if b >= 0:
                total += 1
            
    boxes.append(box)

def ripe():
    while q:
        z, x, y = q.popleft()
        
        for i in range(6):
            z_ = z + dz[i]
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if 0 <= z_ < h and 0 <= x_ < n and 0 <= y_ < m and boxes[z_][x_][y_] == 0:
                boxes[z_][x_][y_] = boxes[z][x][y] + 1
                q.append([z_, x_, y_])


q = deque([])

no = False
for k in range(h):
    for i in range(n):
        for j in range(m):
            if boxes[k][i][j] == 1:
                q.append([k, i, j])

ripe()

day = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if boxes[k][i][j] == 0:
                no = True
            day = max(day, boxes[k][i][j])

if no:
    print(-1)
else:
    print(day-1)