from collections import deque

N = int(input())

board = [[0]*(N+1) for _ in range(N+1)]
snake_self = deque([])

K = int(input())

for _ in range(K):
    x, y = list(map(int, input().split()))
    board[x-1][y-1] = 1

L = int(input())

info = {}

for _ in range(L):
    X, C = input().split(' ')
    info[int(X)] = C

dx = [0, 1,  0, -1]
dy = [1, 0, -1,  0]
direction = 0

x = y = 0
snake_self.append([x, y])

time = 1

for t in range(1, 10001):    
    if (t-1) in info.keys():
        if info[t-1] == 'D':
            if direction < 3:
                direction += 1
            else:
                direction = 0
        elif info[t-1] == 'L':
            if direction > 0:
                direction -= 1
            else:
                direction = 3   
   
   
    nx = snake_self[-1][0] + dx[direction]
    ny = snake_self[-1][1] + dy[direction]            
    
    if 0 <= nx < N and 0 <= ny < N and ([nx, ny] not in snake_self):
        if board[nx][ny] == 1:
            snake_self.append([nx, ny])
            board[nx][ny] = 0
        else:
            snake_self.popleft()
            snake_self.append([nx, ny])
    else:
        break

print(t)