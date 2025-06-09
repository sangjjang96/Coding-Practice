import sys
from collections import deque

ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())

maps = [list(map(str, input())) for _ in range(r)]

def bfs():
    global ans
    
    q = deque([])
    ad = dict()
    ad[maps[0][0]] = 0
    q.append([0, 0, ad])
    
    while q:
        x, y, ad = q.popleft()
        
        ans = max(ans, len(ad.keys()))
        
        if len(ad.keys()) >= ans:
            print(ad)
        
        for d in range(4):
            x_, y_ = x + dx[d], y + dy[d]
            
            if 0 <= x_ < r and 0 <= y_ < c and maps[x_][y_] not in ad.keys():
                ad[maps[x_][y_]] = 0
                q.append([x_, y_, ad])

bfs()
print(ans)