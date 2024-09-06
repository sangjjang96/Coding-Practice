from collections import deque
import sys

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(sys.stdin.readline())

pic = [[] for _ in range(N)]

q_r = deque([])
q_g = deque([])
q_b = deque([])

q_rg = deque([])
q_b_ = deque([])

for i in range(N):
    p = list(map(str, sys.stdin.readline().split()))
    for tmp in p[0][:N]:
        pic[i].append(tmp)

import copy
pic_cb = copy.deepcopy(pic)
    
def bfs_r():
    while q_r:
        x, y = q_r.popleft()
        pic[x][y] = '0'
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < N and pic[new_x][new_y] == 'R':
                pic[new_x][new_y] = '0'
                q_r.append([new_x, new_y])
        
def bfs_rg():
    while q_rg:
        x, y = q_rg.popleft()
        pic[x][y] = '0'
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < N and (pic_cb[new_x][new_y] == 'R' or pic_cb[new_x][new_y] == 'G'):
                pic_cb[new_x][new_y] = '0'
                q_rg.append([new_x, new_y])
    
def bfs_g():
    while q_g:
        x, y = q_g.popleft()
        pic[x][y] = '1'
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < N and pic[new_x][new_y] == 'G':
                pic[new_x][new_y] = '0'
                q_g.append([new_x, new_y])

def bfs_b():
    while q_b:
        x, y = q_b.popleft()
        pic[x][y] = '2'
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < N and pic[new_x][new_y] == 'B':
                pic[new_x][new_y] = '0'
                q_b.append([new_x, new_y])


def bfs_b_():
    while q_b_:
        x, y = q_b_.popleft()
        pic_cb[x][y] = '2'
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < N and pic_cb[new_x][new_y] == 'B':
                pic_cb[new_x][new_y] = '0'
                q_b_.append([new_x, new_y])
    
ans = 0
ans_cb = 0

num_r = 0
for i in range(len(pic)):
    for j in range(len(pic[0])):
        if pic[i][j] == 'R':
            num_r += 1
            q_r.append([i, j])
            bfs_r()

num_g = 0
for i in range(len(pic)):
    for j in range(len(pic[0])):
        if pic[i][j] == 'G':
            num_g += 1
            q_g.append([i, j])
            bfs_g()

num_b = 0
for i in range(len(pic)):
    for j in range(len(pic[0])):
        if pic[i][j] == 'B':
            num_b += 1
            q_b.append([i, j])
            bfs_b()


num_rg = 0
for i in range(len(pic_cb)):
    for j in range(len(pic_cb[0])):
        if (pic_cb[i][j] == 'R' or pic_cb[i][j] == 'G'):
            num_rg += 1
            q_rg.append([i, j])
            bfs_rg()

num_b_ = 0
for i in range(len(pic_cb)):
    for j in range(len(pic_cb[0])):
        if pic_cb[i][j] == 'B':
            num_b_ += 1
            q_b_.append([i, j])
            bfs_b_()

ans = num_r + num_g + num_b
ans_cb = num_rg + num_b
print(ans, ans_cb)