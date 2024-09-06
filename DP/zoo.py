import sys

N = int(sys.stdin.readline())

dp = [0]*(100001)

dp[1] = 3           # 0 1 x
dp[2] = 7           # 0 - 1, x / 1 - 0, x / x - 0, 1, x

if N == 1:
    print(dp[1])
elif N == 2:
    print(dp[2])
else:
    for i in range(3, N+1):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
    
    print(dp[N])
