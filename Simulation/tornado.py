import sys

def rot(prop):
    new_prop = list(reversed(list(zip(*prop))))
    
    return new_prop

left = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
down = rot(left)
right = rot(down)
up = rot(right)

props = [left, down, right, up]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
alphas = [(2, 1), (3, 2), (2, 3), (1, 2)]

n = int(input())

field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 0

x_cur, y_cur = n//2, n//2

d = 0
turn = 2
ran = 0

prop = props[0]

while not (x_cur == 0 and y_cur == 0):
    x_cur += directions[d][0]
    y_cur += directions[d][1]
    
    ran += 1

    sand = field[x_cur][y_cur]
    field[x_cur][y_cur] = 0
    remain = sand
    
    for r in range(5):
        for c in range(5):
            sand_now = int(sand * prop[r][c])
            remain -= sand_now
            
            if 0 <= x_cur + r - 2 < n and 0 <= y_cur + c - 2 < n:
                field[x_cur+r-2][y_cur+c-2] += sand_now
            else:
                ans += sand_now
    
    if 0 <= x_cur + alphas[d][0] - 2 < n and 0 <= y_cur + alphas[d][1] - 2 < n:
        field[x_cur+alphas[d][0]-2][y_cur+alphas[d][1]-2] += remain
    else:
        ans += remain
    
    if ran == turn // 2 or ran == turn:
        d = (d+1) % 4
        prop = props[d]
        if ran == turn:
            ran = 0
            turn += 2
                
print(ans)