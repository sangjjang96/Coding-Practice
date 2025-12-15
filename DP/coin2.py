import sys

n, k = list(map(int, sys.stdin.readline().split()))

coins = []
dp = [0]*(k+1)

for _ in range(n):
    c = int(sys.stdin.readline())
    
    coins.append(c)
    dp[c] = 1

coins.sort()

