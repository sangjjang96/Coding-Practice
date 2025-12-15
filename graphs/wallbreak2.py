import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N, M, K = list(map(int, sys.stdin.readline().split()))

maps = []

for _ in range(N):
    m = list(map(str, sys.stdin.readline()))
    
    m_l = []
    for m_ in m[:M]:
        m_l.append(int(m_))
    
    maps.append(m_l)

def bfs():
    q = deque([])
    q.append([0, 0, 0])
    
    while q:
        x, y, w = q.popleft()
        
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if x_ <= -1 or x_ >= N or y_ <= -1 or y_ >= M:
                continue
            
            if maps[x_][y_] == 1 and w+1 <= K:
                visited[x_][y_][w+1] = visited[x][y][w] + 1
                q.append([x_, y_, w+1])
            
            if maps[x_][y_] == 0 and visited[x_][y_][w] == 0:
                visited[x_][y_][w] = visited[x][y][w] + 1
                q.append([x_, y_, w])
        
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

visited[0][0][0] = 1

ans = bfs()

if ans == None:
    print(-1)
else:
    print(ans)