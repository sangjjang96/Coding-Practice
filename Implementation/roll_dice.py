import sys

n, m, x, y, k = list(map(int, sys.stdin.readline().split()))
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cmd = list(map(int, sys.stdin.readline().split()))
dice = [[0]*3 for _ in range(4)]

for dir in cmd:   
    if dir == 4:
        if x + 1 >= n:
            continue
        x += 1
        mid = dice[0][1]
        for j in range(1, 4):
            tmp = dice[j][1]
            dice[j][1] = mid
            mid = tmp
        dice[0][1] = mid
    elif dir == 3:
        if x - 1 < 0:
            continue
        x -= 1
        mid = dice[3][1]
        for j in range(2, -1, -1):
            tmp = dice[j][1]
            dice[j][1] = mid
            mid = tmp
        dice[3][1] = mid
    elif dir == 2:
        if y - 1 < 0:
            continue
        y -= 1
        mid = dice[3][1]
        for j in range(2, -1, -1):
            tmp = dice[1][j]
            dice[1][j] = mid
            mid = tmp
        dice[3][1] = mid
    elif dir == 1:
        if y + 1 >= n:
            continue
        y += 1
        mid = dice[3][1]
        for j in range(0, 3):
            tmp = dice[1][j]
            dice[1][j] = mid
            mid = tmp
        dice[3][1] = mid
    
    
    if maps[x][y] == 0:
        maps[x][y] = dice[3][1]
    else:
        dice[3][1] = maps[x][y]
        maps[x][y] = 0
    
    print(dice[1][1])