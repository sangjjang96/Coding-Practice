import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

r, c, t = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

for idx in range(t):
    upper = deque([])
    lower = deque([])
    dirts = []
    vents = []
    

    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0:
                dirts.append([i, j, maps[i][j]])
            elif maps[i][j] == -1:
                vents.append([i, j])
    
    upper_x, upper_y = vents[0]
    lower_x, lower_y = vents[1]
    
    # circle_rev
    for i in range(upper_y, c):
        upper.append([upper_x, i])
    for i in range(upper_x-1, -1, -1):
        upper.append([i, c-1])
    for i in range(c-2, upper_y-1, -1):
        upper.append([0, i])
    for i in range(1, upper_x):
        upper.append([i, 0])
        
    # circle
    for i in range(lower_y, c):
        lower.append([lower_x, i])
    for i in range(lower_x+1, r):
        lower.append([i, c-1])
    for i in range(c-2, lower_y-1, -1):
        lower.append([r-1, i])
    for i in range(r-2, lower_x, -1):
        lower.append([i, lower_y])
        
    to_add = [[0]*c for _ in range(r)]

    for dirt in dirts:
        cnt = 0
        x, y = dirt[0], dirt[1]
        
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if 0 <= x_ < r and 0 <= y_ < c and [x_, y_] not in vents:
                to_add[x_][y_] += (maps[x][y] // 5)
                cnt += 1
        
        to_add[x][y] -= ((maps[x][y] // 5) * cnt)
    
    maps += to_add
    
    for i in range(len(upper)):
        x, y = upper[i]
        
        upper[i].append(maps[x][y])
    
    for i in range(len(lower)):
        x, y = lower[i]
        
        lower[i].append(maps[x][y])

    for i in range(len(upper)):
        from_x, from_y, from_num = upper[i]
        
        if i + 1 >= len(upper):
            to_x, to_y, to_num = upper[0]
        else:
            to_x, to_y, to_num = upper[i+1]
        
        if [from_x, from_y] in vents:
            maps[to_x][to_y] = 0
        elif [to_x, to_y] in vents:
            maps[to_x][to_y] = -1
        else:
            maps[to_x][to_y] = from_num
    
    for i in range(len(lower)):
        from_x, from_y, from_num = lower[i]
        
        if i + 1 >= len(lower):
            to_x, to_y, to_num = lower[0]
        else:
            to_x, to_y, to_num = lower[i+1]
        
        if [from_x, from_y] in vents:
            maps[to_x][to_y] = 0
        elif [to_x, to_y] in vents:
            maps[to_x][to_y] = -1
        else:
            maps[to_x][to_y] = from_num

ans = 2
for m in maps:
    ans += sum(m)
print(ans)