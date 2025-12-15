import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

n = int(input())
forests = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

def dfs(x_start, y_start):
    if dp[x_start][y_start]:
        return dp[x_start][y_start]
    
    dp[x_start][y_start] = 1
    
    for d in range(4):
        x_, y_ = x_start+dx[d], y_start+dy[d]
        
        if 0 <= x_ < n and 0 <= y_ < n and forests[x_][y_] > forests[x_start][y_start]:
            dp[x_start][y_start] = max(dp[x_start][y_start], dfs(x_, y_)+1)
    
    return dp[x_start][y_start]

for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            dfs(i, j)

for d in dp:
    ans = max(ans, max(d))

print(ans)