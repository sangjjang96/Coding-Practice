import sys

n, m = list(map(int, sys.stdin.readline().split()))

dp = [[0]*m for _ in range(n)]

fields = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp[0] = fields[0][:]

for i in range(1, m):
    dp[0][i] += dp[0][i-1]

for i in range(1, n):
    t1 = [0]*m              # left
    t2 = [0]*m              # right
    
    for j in range(m):
        if j == 0:
            t1[j] = fields[i][j] + dp[i-1][j]
            t2[m-1-j] = fields[i][m-1-j] + dp[i-1][m-1-j]
            continue
        
        t1[j] = fields[i][j] + max(dp[i-1][j], t1[j-1])
        t2[m-1-j] = fields[i][m-1-j] + max(dp[i-1][m-1-j], t2[m-j])
    
    t = [max(t1[i], t2[i]) for i in range(m)]
    dp[i] = t[:]
    
print(dp[n-1][m-1])