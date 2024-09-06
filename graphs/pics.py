import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, m = list(map(int, sys.stdin.readline().split()))

paper = []
q = deque([])

for _ in range(n):
    pic = list(map(int, sys.stdin.readline().split()))
    paper.append(pic)

def bfs(s):
    while q:
        x, y = q.popleft()
        paper[x][y] = 9
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < n and 0 <= new_y < m and paper[new_x][new_y] == 1:
                paper[new_x][new_y] = 9
                s += 1
                q.append([new_x, new_y])
    
    return s

sizes = []       
num = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            q.append([i, j])
            size = bfs(1)
            sizes.append(size)
            num += 1  

print(num)

if sizes:
    print(max(sizes))
else:
    print(0)