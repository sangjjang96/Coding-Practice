import sys

N = int(sys.stdin.readline())

mats = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

for i in range(N-1):
    dp[i][i+1] = mats[i][0]*mats[i+1][0]*mats[i+1][1]

for i in range(2, N):
    l = 0
    r = i
    
    while r < N:
        dp[l][r] = 2**31
        for k in range(l, r):
            dp[l][r] = min(dp[l][r], dp[l][k] + dp[k+1][r] + mats[l][0]*mats[k][1]*mats[r][1])
        l += 1
        r += 1

print(dp[0][N-1])