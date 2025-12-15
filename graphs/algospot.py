import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = list(map(int, sys.stdin.readline().split()))

maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]
    
broken = int(1e9)
counts = [[int(1e9)]*n for _ in range(m)]

def bfs():
    global broken
    global counts
    
    visited = [[0]*n for _ in range(m)]
    visited[0][0] = 1
    
    counts[0][0] = 0
    
    q = deque([])
    q.append([0, 0, 0])
    
    while q:
        x, y, cnt = q.popleft()
        
        if [x, y] == [m-1, n-1]:
            broken = min(broken, cnt)
        
        for i in range(4):
            x_ , y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < m and 0 <= y_ < n:
                if maze[x_][y_] == 0:
                    counts[x_][y_] = min(counts[x_][y_], cnt)
                else:
                    counts[x_][y_] = min(counts[x_][y_], cnt+1)
                
                if not visited[x_][y_]:
                    visited[x_][y_] = 1
                    if maze[x_][y_] == 0:
                        q.appendleft([x_, y_, cnt])
                    else:
                        q.append([x_, y_, cnt+1])
        
bfs()

print(min(broken, counts[m-1][n-1]))