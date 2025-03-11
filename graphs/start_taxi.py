import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

inf = int(1e9)

n, m, fuel = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

taxi_x, taxi_y = list(map(int, sys.stdin.readline().split()))

customers = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

import copy

def bfs(start_x, start_y):
    q = deque([])
    
    q.append([start_x, start_y])
    visited = [[False]*n for _ in range(n)]
    visited[start_x][start_y] = True
    
    maps_tmp = copy.deepcopy(maps)
    maps_tmp[start_x][start_y] = 10
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if 0 <= x_ < n and 0 <= y_ < n and not visited[x_][y_] and maps[x_][y_] == 0:
                visited[x_][y_] = True
                maps_tmp[x_][y_] = maps_tmp[x][y] + 1
                q.append([x_, y_])
    
    return maps_tmp


def search(start_x, start_y):
    return bfs(start_x, start_y)

for i in range(m):
    customers[i].append(0)

breaked = False

for num in range(m):
    distance = 0
    map_result = search(taxi_x-1, taxi_y-1)

    for idx, (x, y, x_, y_, r) in enumerate(customers):
        ran = map_result[x-1][y-1] - 10
        
        if customers[idx][4] != inf:
            customers[idx][4] = ran
    customers.sort(key=lambda x: (x[4], x[0]))
    
    if customers[0][4] == inf:
        print('inf')
        breaked = True
        print(-1)
        break
    
    if map_result[customers[0][0]-1][customers[0][1]-1] == 0 and [taxi_x, taxi_y] != [customers[0][0], customers[0][1]]:
        breaked = True
        print(-1)
        break
    
    dist = (map_result[customers[0][0]-1][customers[0][1]-1] - 10)
    fuel -= dist
    if fuel < 0:
        breaked = True
        print(-1)
        break
    
    distance += dist

    map_result = search(customers[0][0]-1, customers[0][1]-1)

    if map_result[customers[0][2]-1][customers[0][3]-1] == 0 and [customers[0][0], customers[0][1]] != [customers[0][2], customers[0][3]]:
        breaked = True
        print(-1)
        break
    
    dist = (map_result[customers[0][2]-1][customers[0][3]-1] - 10)
    fuel -= dist
    if fuel < 0:
        breaked = True
        print(-1)
        break

    distance += dist
    
    customers[0][4] = inf
    fuel += (dist * 2)
    
    taxi_x = customers[0][2]
    taxi_y = customers[0][3]

if not breaked:
    print(fuel)