import sys
from collections import deque

def bfs(answer, num_eat, shark_size, num_fish):
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            
            if 0 <= x_ < N and 0 <= y_ < N and space[x_][y_] in [0, 1, 2, 3, 4, 5, 6]:
                if space[x_][y_] == 0:
                    space[x][y] = 0
                    space[x_][y_] = 9
                    answer += 1
                    q.append([x_, y_])
                else:
                    if shark_size >= space[x_][y_]:
                        num_eat += space[x_][y_]
                        if num_eat >= shark_size:
                            num_eat -= shark_size
                            shark_size += 1
                        
                        space[x][y] = 0
                        space[x_][y_] = 9
                        num_fish -= 1
                        break
    
    return answer, num_eat, shark_size, num_fish

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


N = int(sys.stdin.readline())

answer = 0
space = []
shark_size = 2
num_eat = 0

for _ in range(N):
    space.append(list(map(int, sys.stdin.readline().split())))
    
q = deque([])

num_fish = 0

for i in range(N):
    for j in range(N):
        if space[i][j] in [1, 2, 3, 4, 5, 6]:
            num_fish += 1

while num_fish > 0:
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                q.append([i, j])
                answer, num_eat, shark_size, num_fish = bfs(answer, num_eat, shark_size, num_fish)
                
    print(num_fish)
    
print(answer)