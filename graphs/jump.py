import sys
from collections import deque

dx = [0, 1]
dy = [1, 0]

N = int(sys.stdin.readline())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visit = [[0]*N for _ in range(N)]
visit[0][0] = 1

q = deque([])

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(visit[i][j])
            break
        
        if j + maps[i][j] < N:
            visit[i][j + maps[i][j]] += visit[i][j]
        
        if i + maps[i][j] < N:
            visit[i + maps[i][j]][j] += visit[i][j]
            