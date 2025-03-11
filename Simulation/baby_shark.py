import sys
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n = int(sys.stdin.readline())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            shark_x, shark_y = i, j

            
def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    queue = deque([[x,y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ii, jj = i + dx[idx] , j + dy[idx]

            if 0 <= ii and ii < n and 0 <= jj and jj < n and visited[ii][jj] == 0:

                if maps[x][y] > maps[ii][jj] and maps[ii][jj] != 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif maps[x][y] == maps[ii][jj]:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
                elif maps[ii][jj] == 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
                    

    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))
    
    
def search(x, y):
    return bfs(x, y)

cnt = 0
i, j = shark_x, shark_y
size = [2, 0]

while True:
    maps[i][j] = size[0]
    cand = deque(bfs(i,j))
    
    if not cand:
        break
        

    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1
    

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    maps[i][j] = 0
    i, j = xx, yy
        
print(cnt)