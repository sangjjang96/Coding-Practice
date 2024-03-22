T = int(input())

from collections import deque

def bfs():
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    
    q = deque()
    q.append((now_x, now_y))
    
    while q:
        x, y = q.popleft()
        if x == to_x and y == to_y:
            return matrix[x][y] - 1
        
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0<=new_x<I and 0<=new_y<I and matrix[new_x][new_y] == 0:
                matrix[new_x][new_y] = matrix[x][y] + 1
                q.append((new_x, new_y))

for  _ in range(T):
    I = int(input())
 
    now_x, now_y = list(map(int, input().split()))
    to_x, to_y = list(map(int, input().split()))
    
    matrix = [[0]*I for _ in range(I)]
    matrix[now_x][now_y] = 1
    print(bfs())
    