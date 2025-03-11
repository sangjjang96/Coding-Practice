import sys
from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

n = int(input())

maps = []

for _ in range(n):
    m = sys.stdin.readline().rstrip()
    
    l = []
    for m_ in m:
        l.append(int(m_))
    maps.append(l)
    
def bfs(x, y, idx):
    cnt = 1
    q = deque([])
    visited = [[0]*n for _ in range(n)]
    q.append([x, y, idx])
    
    while q:
        xx, yy, idx_ = q.popleft()
        
        maps[xx][yy] = idx_
        visited[xx][yy] = 1
        
        for i in range(4):
            x_ = xx + dx[i]
            y_ = yy + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < n and maps[x_][y_] == 1 and visited[x_][y_] == 0:
                cnt += 1
                q.append([x_, y_, idx_])
    print(idx, cnt)

idx = 2
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            bfs(i, j, idx)
            idx += 1

ans = [0] * idx

for ma in maps:
    for m in ma:
        if m > 0:
            ans[m] += 1
    
ans.sort()

print(len(ans)-2)
for a in ans:
    if a > 0:
        print(a)