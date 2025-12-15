import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = list(map(int, sys.stdin.readline().split()))

keys = [[[] for _ in range(n+1)] for _ in range(n+1)]
visited = [[0]*(n+1) for _ in range(n+1)]
light = [[0]*(n+1) for _ in range(n+1)]

q = deque()
q.append((1, 1))

visited[1][1] = 1
light[1][1] = 1
ans = 1

for _ in range(m):
    x, y, a, b = list(map(int, sys.stdin.readline().split()))
    
    keys[x][y].append((a, b))

while q:
    x, y = q.popleft()
    
    for a, b in keys[x][y]:
        if not light[a][b]:
            light[a][b] = 1
            ans += 1
            
            for i in range(4):
                a_ = a + dx[i]
                b_ = b + dy[i]
                
                if 1 <= a_ <= n and 1 <= b_ <= n and visited[a_][b_]:
                    q.append((a_, b_))
    
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        
        if 1 <= x_ <= n and 1 <= y_ <= n:
            if not visited[x_][y_] and light[x_][y_]:
                visited[x_][y_] = 1
                q.append((x_, y_))

print(ans)
    