import sys

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n = int(sys.stdin.readline())
seats = [[0]*n for _ in range(n)]
students = [list(map(int, sys.stdin.readline().split())) for _ in range(n**2)]


for student in students:
    avail = []
    
    for i in range(n):
        for j in range(n):
            if seats[i][j] == 0:
                prefer, empty = 0, 0
                
                for k in range(4):
                    i_ = i + dx[k]
                    j_ = j + dy[k]
                    
                    if 0 <= i_ < n and 0 <= j_ < n:
                        if seats[i_][j_] in student[1:]:
                            prefer += 1
                        
                        if seats[i_][j_] == 0:
                            empty += 1
                avail.append([i, j, prefer, empty])
    
    avail.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    seats[avail[0][0]][avail[0][1]] = student[0]

ans = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for i in range(n):
    for j in range(n):
        cnt = 0
        
        for k in range(4):
            i_ = i + dx[k]
            j_ = j + dy[k]
            
            if 0 <= i_ < n and 0 <= j_ < n:
                if seats[i_][j_] in students[seats[i][j] - 1]:
                    cnt += 1
        
        ans += score[cnt]

print(ans)