T = int(input())

dp = [[0]*31 for _ in range(31)]

for i in range(1, 31):
    dp[i][i] = 1

for i in range(1, 31):
    dp[1][i] = i

for i in range(1, 31):
    for j in range(1, 31):
        if i == j or i == 1:
            continue
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for i in range(T):
    N, M = list(map(int, input().split()))
    print(dp[N][M])