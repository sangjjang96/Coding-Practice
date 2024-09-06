import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))

office = []

for _ in range(N):
    office.append(list(map(int, sys.stdin.readline().split())))


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cctv = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]

obj = deque([])
answer = 0


for i in range(N):
    for j in range(M):
        if office[i][j] in [1, 2, 3, 4, 5]:
            obj.append((office[i][j], i, j))
        if office[i][j] == 0:
            answer += 1

pos = obj

def move(y, x, dir, space_copy):
    for d in dir:
        ny, nx = y, x
        
        while True:
            nx += dx[d]
            ny += dy[d]
            
            if ny < 0 or ny >= N or nx < 0 or nx >= M or space_copy[ny][nx] == 6:
                break
            if space_copy[ny][nx] != 0:
                continue
            space_copy[ny][nx] = '#'

def z_cnt(space_copy):
    global answer
    cnt = 0
    for i in space_copy:
        cnt += i.count(0)
    answer = min(answer , cnt)
    
def dfs(level, space):
    space_copy = [[j for j in space[i]] for i in range(N)]
    
    if level == len(pos):
        z_cnt(space_copy)
        return
    
    num, y, x = pos[level]
    
    for d in cctv[num]:
        move(y, x, d, space_copy)
        dfs(level+1, space_copy)
        space_copy = [[j for j in space[i]] for i in range(N)]
        
dfs(0, office)
print(answer)