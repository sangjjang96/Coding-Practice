import sys, copy
from collections import deque

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

reverse = [0, 2, 1, 4, 3]

ans = 0

R, C, M = list(map(int, sys.stdin.readline().split()))

maps = [[] for _ in range(R+1)]

for i in range(R+1):
    for j in range(C+1):
        maps[i].append([])

for _ in range(M):
    r, c, s, d, z = list(map(int, sys.stdin.readline().split()))
    
    maps[r][c].append([z, s, d])

for sec in range(1, C+1):
    
    # catch shark
    for i in range(1, R+1):
        if maps[i][sec]:
            val = maps[i][sec][0]
            ans += val[0]
            maps[i][sec].remove(val)
            break
        
    maps_new = [[[] for _ in range(C+1)] for _ in range(R+1)]
    
    # move shark
    for i in range(1, R+1):
        for j in range(1, C+1):
            if maps[i][j]:
                size, speed, direction = maps[i][j][0]
                
                spd_tmp = speed
                
                if 1 <= speed * dx[direction] + i <= R and 0 <= speed * dy[direction] + j <= C:
                    x, y, direction = speed * dx[direction] + i, speed * dy[direction] + j, direction
                else:
                    if direction == 1:
                        speed += (R - i)
                    elif direction == 2:
                        speed += i-1
                    elif direction == 3:
                        speed += j-1
                    elif direction == 4:
                        speed += (C - j)
                        
                    if direction == 3 or direction == 4:
                        k = (speed-1) // (C-1)
                        go = (speed - k * (C-1)) % C
                    else:
                        k = (speed-1) // (R-1)
                        go = (speed - k * (R-1)) % R
                    
                    if k % 2 == 1:
                        direction = reverse[direction]
                    
                    x, y = i, j
                    
                    if direction == 1:
                        x = R
                    elif direction == 2:
                        x = 1
                    elif direction == 3:
                        y = 1
                    elif direction == 4:
                        y = C
                    
                    x += dx[direction] * go
                    y += dy[direction] * go
                        
                # eat shark
                if not maps_new[x][y]:
                    maps_new[x][y].append([size, spd_tmp, direction])
                else:
                    if maps_new[x][y][0][0] > size:
                        continue
                    else:
                        maps_new[x][y][0] = [size, spd_tmp, direction]
    
    maps = [m[:] for m in maps_new]

print(ans)