import sys
from collections import deque

horse_x = [-2, -2, -1, 1, 2, 2, 1, -1]
horse_y = [-1, 1, 2, 2, 1, -1, -2, -2]

monkey_x = [-1, 0, 1, 0]
monkey_y = [0, 1, 0, -1]

K = int(sys.stdin.readline())

w, h = list(map(int, sys.stdin.readline().split()))

board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

def bfs():
    visited = [[[False] * (K+1) for _ in range(w)] for _ in range(h)]
    visited[0][0][K] = True
    queue = deque([(0, 0, K, 0)])
 
    while queue:
        x, y, k, move = queue.popleft()
 
        # 목표 지점 도달
        if x == h-1 and y == w-1:
            return move
 
        # 말처럼 이동하는 경우 - k(남은 움직일 수 있는 이동 횟수)가 1 이상인지 확인
        if k:
            for i in range(8):
                nx = x + horse_x[i]
                ny = y + horse_y[i]
 
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][k-1] and board[nx][ny] != 1:
                    visited[nx][ny][k-1] = True
                    queue.append((nx, ny, k-1, move+1)) # 말처럼 움직인 횟수 1 차감, 이동 횟수 1 증감
 
        # 원숭이 처럼 상하좌우로 이동하는 경우
        for i in range(4):
            nx = x + monkey_x[i]
            ny = y + monkey_y[i]
 
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][k] and board[nx][ny] != 1:
                visited[nx][ny][k] = True
                queue.append((nx, ny, k, move+1))
    return -1 
                
print(bfs())