N, K = list(map(int, input().split()))

graph = []

for i in range(1, N+1):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x_, y_ = q.popleft()
        
        for i in range(4):
            new_x = x_ + dx[i]
            new_y = y_ + dy[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= K:
                continue
            if graph[new_x][new_y] == 0:
                continue
            
            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = graph[x_][y_] + 1
                q.append((new_x, new_y))
    
    return graph[N-1][K-1]    

print(bfs(0, 0))