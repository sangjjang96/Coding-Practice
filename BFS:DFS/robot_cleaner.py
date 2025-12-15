import sys
from collections import deque
from itertools import *

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    cnt = int(1e9)
    
    w, h = list(map(int, sys.stdin.readline().split()))
    
    if w == 0 and h == 0:
        break
    
    room = [list(map(str, sys.stdin.readline())) for _ in range(h)]
    
    dirties = []
    
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                start_x, start_y = i, j
            elif room[i][j] == '*':
                dirties.append([i, j])
    
    def bfs(x_start, y_start, dirty_x, dirty_y):
        q = deque([])
        visited = [[0]*w for _ in range(h)]
        
        q.append([x_start, y_start, 0])
        visited[x_start][y_start] = 1
        
        while q:
            x, y, c = q.popleft()
            
            if [x, y] == [dirty_x, dirty_y]:
                return c
            
            for i in range(4):
                x_, y_ = x + dx[i], y + dy[i]
                
                if 0 <= x_ < h and 0 <= y_ < w and room[x_][y_] != 'x' and not visited[x_][y_]:
                    visited[x_][y_] = 1
                    q.append([x_, y_, c+1])
        
        return int(1e9)
    
    for perm in deque(permutations(dirties, len(dirties))):
        cnt_tmp = 0
        for idx, p in enumerate(perm):
            if idx == 0:
                cnt_tmp += bfs(start_x, start_y, p[0], p[1])
            else:
                cnt_tmp += bfs(perm[idx-1][0], perm[idx-1][1], perm[idx][0], perm[idx][1])

        cnt = min(cnt, cnt_tmp)
    
    
    if cnt >= int(1e9):
        print(-1)
    else:
        print(cnt)