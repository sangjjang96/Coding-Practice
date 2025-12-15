import sys
sys.setrecursionlimit(10 ** 6)

n, m = list(map(int, sys.stdin.readline().split()))

ladders = {}
snakes = {}

for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    
    ladders[x] = y

for _ in range(m):
    u, v = list(map(int, sys.stdin.readline().split()))
    
    snakes[u] = v


now = 1

dp = [int(1e9)]*(101)

def dfs(start, cnt):
    for i in range(1, 7):
        ret = start + i
        
        if ret in ladders.keys():
            ret = ladders[ret]
        
        if ret in snakes.keys():
            ret = snakes[ret]
        
        cnt_ = cnt + 1
        if ret >= 100:
            dp[100] = min(dp[100], cnt_)
            return

        if cnt_ < dp[ret]:
            dp[ret] = cnt_
            dfs(ret, cnt_)

dfs(now, 0)

print(dp[100])