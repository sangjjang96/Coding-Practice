import sys

price = int(sys.stdin.readline())

dp = [-1]*(price+8)

dp[2]=1
dp[4]=2
dp[5]=1
dp[6]=3
dp[7]=2
dp[8]=4

for i in range(9, price+1):
    dp[i] = min(dp[i-2], dp[i-5])+1

print(dp[price])