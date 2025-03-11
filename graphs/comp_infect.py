import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N, K = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

S, X, Y = list(map(int, sys.stdin.readline().split()))

def bfs():
    while q:
        num, t, x, y = q.popleft()
        
        if t == S:
            break
        
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if 0 <= x_ < N and 0 <= y_ < N and maps[x_][y_] == 0:
                maps[x_][y_] = num
                q.append([num, t+1, x_, y_])

virus = []

for i in range(N):
    for j in range(N):
        if maps[i][j] != 0:
            virus.append([maps[i][j], 0, i, j])

virus.sort()
q = deque(virus)

bfs()

print(maps[X-1][Y-1])