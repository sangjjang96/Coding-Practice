import sys

N, M = list(map(int, sys.stdin.readline().split()))

r, c, d = list(map(int, sys.stdin.readline().split()))

answer = 0
room = []

    # N E S W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))

visited = [[0]*M for _ in range(N)]    

visited[r][c] = 1
answer += 1

direction = d

while True:
    flag = 0

    for _ in range(4):
        direction = (direction + 3) % 4
        new_r = r + dx[direction]
        new_c = c + dy[direction]
        
        if 0 <= new_r < N and 0 <= new_c < M and room[new_r][new_c] == 0:
            if visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                answer += 1
                r = new_r
                c = new_c
                flag = 1
                break
            
    if flag == 0:
        if room[r-dx[direction]][c-dy[direction]] == 1:
            print(answer)
            break
        else:
            r = r - dx[direction]
            c = c - dy[direction]