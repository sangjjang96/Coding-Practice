import sys
from collections import deque

ans = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, sys.stdin.readline().split())

boards = [list(map(lambda x: ord(x)-65, sys.stdin.readline())) for _ in range(r)]

alpha = [False]*26

ans = 1

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    
    for i in range(4):
        x_, y_ = x + dx[i], y + dy[i]
        
        if 0 <= x_ < r and 0 <= y_ < c and not alpha[boards[x_][y_]]:
            alpha[boards[x_][y_]] = True
            dfs(x_, y_, cnt+1)
            alpha[boards[x_][y_]] = False

alpha[boards[0][0]] = True
dfs(0, 0, ans)
print(ans)