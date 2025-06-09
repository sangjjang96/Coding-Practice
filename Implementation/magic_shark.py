import sys

ans = 0

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0 ,-1]

diag_x = [-1, -1, 1, 1]
diag_y = [-1, 1, 1, -1]

n, m = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

moves = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

clouds = [[n-2, 0], [n-1, 0], [n-2, 1], [n-1, 1]]

for move in moves:
    direction, steps = move
    
    for _ in range(steps):
        for cloud in clouds:
            cloud[0] += dx[direction]
            cloud[1] += dy[direction]
    
            if cloud[0] < 0:
                cloud[0] += n
            elif cloud[0] >= n:
                cloud[0] -= n
            
            if cloud[1] < 0:
                cloud[1] += n
            elif cloud[1] >= n:
                cloud[1] -= n
    
    for cloud in clouds:
        maps[cloud[0]][cloud[1]] += 1
    
    for cloud in clouds:
        water = 0
        
        for i in range(4):
            new_x = cloud[0] + diag_x[i]
            new_y = cloud[1] + diag_y[i]
            
            if 0 <= new_x < n and 0 <= new_y < n and maps[new_x][new_y] > 0:
                water += 1
        
        maps[cloud[0]][cloud[1]] += water
    
    clouds_tmp = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 2 and [i, j] not in clouds:
                maps[i][j] -= 2
                clouds_tmp.append([i, j])
    
    clouds = clouds_tmp

for ma in maps:
    ans += sum(ma)

print(ans)