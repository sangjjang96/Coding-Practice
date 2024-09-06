N, K = list(map(int, input().split()))

glass = []

for _ in range(N):
    glass.append(list(map(int, input().split())))
    
S, X, Y = list(map(int, input().split()))

from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def bfs(virus):
    while q:
        x_, y_ = q.popleft()
        
        if 0 <= x_ < N and 0 <= y_ < N and glass[x_][y_] == 0:
            glass[x_][y_] = virus 

import copy        

for t in range(S):
    for virus in range(1, K+1):
        glass_tmp = copy.deepcopy(glass)
        q = deque([])
        for x in range(len(glass)):
            for y in range(len(glass[0])):
                if glass_tmp[x][y] == virus:
                    for i in range(4):
                        q.append([x + dx[i], y + dy[i]])
                    bfs(virus)

print(glass[X-1][Y-1])