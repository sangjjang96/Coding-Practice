import sys
sys.setrecursionlimit(1000)

n = int(sys.stdin.readline().rstrip())

scv = list(map(int, sys.stdin.readline().split()))

for _ in range(3-n):
    scv.append(0)

dp = {}
def dfs(a, b, c):
    if (a, b, c) in dp:
        return dp[(a, b, c)]
    
    if (a, b, c) == (0, 0, 0):
        return 0
    
    ans = min(
        dfs(max(a-9, 0), max(b-3, 0), max(c-1, 0)),
        dfs(max(a-9, 0), max(b-1, 0), max(c-3, 0)),
        dfs(max(a-3, 0), max(b-9, 0), max(c-1, 0)),
        dfs(max(a-3, 0), max(b-1, 0), max(c-9, 0)),
        dfs(max(a-1, 0), max(b-9, 0), max(c-3, 0)),
        dfs(max(a-1, 0), max(b-3, 0), max(c-9, 0))
    ) + 1
    
    dp[(a, b, c)] = ans
    return ans
    
print(dfs(*scv))