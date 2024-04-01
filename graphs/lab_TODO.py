from collections import deque

N, M = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

graph = []
q = deque([])

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            q.append([i, j])

def bfs():
    while q:
        x_, y_ = q.popleft()
        
        for i in range(4):
            new_x = x_ + dx[i]
            new_y = y_ + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < M and graph[new_x][new_y] == 0:
                graph[new_x][new_y] = graph[x_][y_]
                q.append([new_x, new_y])

bfs()
      
for g in graph:
    print(g)
print()

for i in graph:
    for j in i:
        if j == 0:
            ans += 1
            
print(ans)