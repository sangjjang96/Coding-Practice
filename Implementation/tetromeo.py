import sys

n, m = list(map(int, sys.stdin.readline().split()))

papers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

def dfs(N, tmp, lst):
    global ans
    
    if N == 4:
        ans = max(ans, tmp)
        return
    
    for x, y in lst:
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < m and visited[x_][y_] == 0:
                visited[x_][y_] = 1
                dfs(N+1, tmp + papers[x_][y_], lst + [(x_, y_)])
                visited[x_][y_] = 0
                
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(1, papers[i][j], [(i, j)])

print(ans)