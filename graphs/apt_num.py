from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

N = int(input())

maps = [[] for _ in range(N)]

for idx in range(N):
    apt = list(map(str, input().split()))

    for a in apt[0]:
        maps[idx].append(int(a))

q = deque([])

def bfs(num):
    while q:
        x, y = q.popleft()
        
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 1:
                maps[nx][ny] = num
                
                q.append([nx, ny])

n = 2

while True:
    num_one = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                q.append([i, j])
                bfs(n)
                n += 1
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                num_one += 1
    
    if num_one == 0:
        break

print(n-2)

numbers = []
numbers.sort()
for num in range(2, n):
    number = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == num:
                number += 1
    numbers.append(number)

for n in numbers:
    print(n)