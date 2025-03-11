from collections import deque
from itertools import combinations
import copy
import sys

N, M = list(map(int, sys.stdin.readline().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

graph = []
q = deque([])

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(graph):
    q = deque([[i, j] for i in range(N) for j in range(M) if graph[i][j] == 2])
    
    while q:
        x_, y_ = q.popleft()
        
        for i in range(4):
            new_x = x_ + dx[i]
            new_y = y_ + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < M and tmp[new_x][new_y] == 0:
                tmp[new_x][new_y] = 2
                q.append([new_x, new_y])
    
    global ans
    count = sum([i.count(0) for i in graph])
    ans = max(ans, count)

x_y = [[x, y] for x in range(N) for y in range(M) if not graph[x][y]]

for c in combinations(x_y, 3):
    tmp = copy.deepcopy(graph)
    for x, y in c:
        tmp[x][y] = 1
    bfs(tmp)

print(ans)