import sys

M, N, K = list(map(int, sys.stdin.readline().split()))

paper = [[1]*(N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 0

from collections import deque

q = deque([])

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(s):
    while q:
        x, y = q.popleft()
        paper[x][y] = 9
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < M and 0 <= new_y < N and paper[new_x][new_y] == 1:
                paper[new_x][new_y] = 9
                q.append([new_x, new_y])
                s += 1
    return s

ans = []

for i in range(len(paper)):
    for j in range(len(paper[0])):
        if paper[i][j] == 1:
            s = 1
            q.append([i, j])
            s = bfs(s)
            ans.append(s)
    
ans.sort()
print(len(ans))
for a in ans:
    print(a, end=' ')