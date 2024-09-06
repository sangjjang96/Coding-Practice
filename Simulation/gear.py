import sys
from collections import deque

g = []

for i in range(4):
    g.append(deque(list(input())))

K = int(input())
R = [list(map(int, input().split())) for _ in range(K)]

def left(num, direction):
    if num < 0:
        return
    if g[num][2] != g[num+1][6]:
        left(num-1, -direction)
        g[num].rotate(direction)

def right(num, direction):
    if num > 3:
        return
    
    if g[num][6] != g[num-1][2]:
        right(num+1, -direction)
        g[num].rotate(direction)
    
for i in range(K):
    num = R[i][0]-1
    direction = R[i][1]
    
    left(num-1, -direction)
    right(num+1, -direction)
    g[num].rotate(direction)

ans = 0

if g[0][0] == '1':
    ans += 1
if g[1][0] == '1':
    ans += 2
if g[2][0] == '1':
    ans += 4
if g[3][0] == '1':
    ans += 8
    
print(ans)