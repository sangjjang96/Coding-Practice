import sys
from collections import deque

ans = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(sys.stdin.readline())

maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

def bfs():
    global ans
    
    q = deque(())
    visited = [[-1] * n for _ in range(n)]
    
    q.append((0, 0))
    visited[0][0] = 0
    
    while q:
        x, y = q.popleft()
        
        if [x, y] == [n-1, n-1]:
            ans = visited[x][y]
            return
        
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < n and visited[x_][y_] == -1:
                if maps[x_][y_] == 1:
                    visited[x_][y_] = visited[x][y]
                    q.appendleft((x_, y_))
                else:
                    visited[x_][y_] = visited[x][y]+1
                    q.append((x_, y_))
                
bfs()
print(ans)
            