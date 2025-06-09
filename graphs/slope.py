import sys
sys.setrecursionlimit(10 ** 9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < m and maps[x][y] > maps[x_][y_]:
                dp[x][y] += bfs(x_, y_)
        
    return dp[x][y]

paths = []

n, m = map(int, sys.stdin.readline().split())
dp = [[-1]*m for _ in range(n)]

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = bfs(0, 0)

print(ans)