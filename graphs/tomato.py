INF = int(1e9)

M, N = map(int,input().split())

from collections import deque
graph = []
q = deque([])
ans = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])

from collections import deque

def bfs():    
    while q:
        x_, y_ = q.popleft()
        
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x_][y_] + 1
                q.append([nx, ny])

bfs()
    
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    
    ans = max(ans, max(i))
            
print(ans-1) 