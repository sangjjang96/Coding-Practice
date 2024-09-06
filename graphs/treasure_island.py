import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))

maps = []
q = deque([])

for _ in range(N):
    s = sys.stdin.readline()
    
    strs = []
    for ss in s:
        strs.append(ss)
    maps.append(strs[:M])
    
def bfs():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    
    max_length = 0
    visited = [[0]*M for _ in range(N)]
    land = [[1]*M for _ in range(N)]
            
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                land[nx][ny] = land[x][y] + 1
                q.append([nx, ny])
    
    for la in land:
        for l in la:
            max_length = max(l, max_length)
    
    return max_length


answer = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(N):
        for j in range(M):
            if maps[i][j] == 'L':
                num_l = 0
                for k in range(4):
                    i_ = i + dx[k]
                    j_ = j + dy[k]
                    
                    if 0 <= i_ < N and 0 <= j_ < M and maps[i_][j_] == 'L':
                        num_l += 1
                
                if num_l <= 2:
                    q.append([i, j])
                    ml = bfs()
                    answer = max(ml, answer)

print(answer-1)
