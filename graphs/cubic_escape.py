import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())

maps = [[0]*m for _ in range(n)]

r_start_x, r_start_y = -1, -1
b_start_x, b_start_y = -1, -1
end_x, end_y = -1, -1

for i in range(n):
    tmp = list(map(str, input()))
    
    for j in range(len(tmp)):
        if tmp[j] == '#':
            maps[i][j] = 1
        elif tmp[j] == '.':
            maps[i][j] = 0
        elif tmp[j] == 'O':
            maps[i][j] = 0
            end_x, end_y = i, j
        elif tmp[j] == 'R':
            maps[i][j] = 0
            r_start_x, r_start_y = i, j
        elif tmp[j] == 'B':
            maps[i][j] = 0
            b_start_x, b_start_y = i, j

print(r_start_x, r_start_y)
print(b_start_x, b_start_y)
print(end_x, end_y)

def bfs():
    q = deque([])
    
    visited = [[0] * m for _ in range(n)]
    
    q.append([r_start_x, r_start_y, b_start_x, b_start_y, visited, [[r_start_x, r_start_y]]])
    
    while q:
        r_x, r_y, b_x, b_y, visited, path = q.popleft()
        
        if [r_x, r_y] == [end_x, end_y]:
            print('Red Done')
            if [b_x, b_y] == [end_x, end_y]:
                print('Blue Done')
                return -1
            print(path)
            return len(path)-1

        if [b_x, b_y] == [end_x, end_y]:
            print('Blue Only')
            return -1

        visited_tmp = [v[:] for v in visited]
        
        visited_tmp[r_x][r_y] = 1
        
        for d in range(4):
            while 
            r_x_ = r_x + dx[d]
            r_y_ = r_y + dy[d]
            b_x_ = b_x + dx[d]
            b_y_ = b_y + dy[d]
            
            r_x_f, r_y_f = -1, -1
            b_x_f, b_y_f = -1, -1
            if maps[r_x_][r_y_] == 0 and not visited_tmp[r_x_][r_y_]:
                visited_tmp[r_x_][r_y_] = 1
                r_x_f, r_y_f = r_x_, r_y_
            else:
                r_x_f, r_y_f = r_x, r_y
                
            if maps[b_x_][b_y_] == 0:
                b_x_f, b_y_f = b_x_, b_y_
            else:
                b_x_f, b_y_f = b_x, b_y
            
            if [r_x_f, r_y_f] != [r_x, r_y]:
                q.append([r_x_f, r_y_f, b_x_f, b_y_f, visited_tmp, path + [[r_x_f, r_y_f]]])


ret = bfs()

if ret <= 10 and ret != -1:
    print(ret)
else:
    print(-1)