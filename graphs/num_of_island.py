from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, 1, 1, -1, -1, 1, 1]

def bfs(x, y):
    q = deque([])
    q.append([x, y])
    maps[x][y] = 0
    
    while q:
        x_, y_ = q.popleft()
        
        for i in range(8):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append([nx, ny])

while True:
    try:
        w, h = list(map(int, input().split()))

        maps = []

        for _ in range(h):
            maps.append(list(map(int, input().split())))

        ans = 0
        for i in range(h):
            for j in range(w):
                if maps[i][j] == 1:
                    bfs(i, j)
                    ans += 1

        print(ans)
    except EOFError:
        break