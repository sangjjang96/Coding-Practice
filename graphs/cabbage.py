from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):    
    q = deque([])
    q.append([x, y])
    ground[x][y] = 0
    
    while q:
        x_, y_ = q.popleft()
        
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and ground[nx][ny] == 1:
                q.append([nx, ny])
                ground[nx][ny] = 0
                
T = int(input())

for _ in range(T):
    M, N, K = list(map(int, input().split()))
    ground = [[0] * N for _ in range(M)]
    ans = 0

    for _ in range(K):
        x, y = list(map(int, input().split()))
        ground[x][y] = 1

    for i in range(M):
        for j in range(N):
            if ground[i][j] == 1:
                bfs(i, j)
                ans += 1 

    print(ans)