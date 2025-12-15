import sys

n, m = list(map(int, sys.stdin.readline().split()))

A = [0] + list(map(int, sys.stdin.readline().split()))

C = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0]*(sum(C)+1) for _ in range(n+1)]

ans = sum(C)

for i in range(1, n+1):
    for j in range(1, sum(C)+1):
        dp[i][j] = dp[i-1][j]
    
    for j in range(C[i], sum(C)+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-C[i]] + A[i])
        
        if dp[i][j] > m:
            ans = min(ans, j)

if m != 0:
    print(ans)
else:
    print(0)