import sys

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = list(map(int, sys.stdin.readline().split()))

food = [[5]*n for _ in range(n)]

A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

trees = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

ground = [[[] for _ in range(n)] for _ in range(n)]

        
for tree in trees:
    ground[tree[0]-1][tree[1]-1].append(tree[2])
    
for _ in range(k):
    died = []
    
    # Spring / Summer
    for i in range(n):
        for j in range(n):
            if len(ground[i][j]) > 0:
                ground[i][j].sort()

                for idx, t in enumerate(ground[i][j]):
                    if t <= food[i][j]:
                        ground[i][j][idx] += 1
                        food[i][j] -= t
                    else:
                        for die in ground[i][j][idx:]:
                            food[i][j] += (die // 2)
                        ground[i][j] = ground[i][j][:idx]
                        break
    
    # Autumn
    for i in range(n):
        for j in range(n):
            if len(ground[i][j]) > 0:
                for g in ground[i][j]:
                    if g % 5 == 0:                        
                        for d in range(8):
                            x_, y_ = i + dx[d], j + dy[d]
                        
                            if 0 <= x_ < n and 0 <= y_ < n:
                                ground[x_][y_].append(1)

    # Winter
    for i in range(n):
        for j in range(n):
            food[i][j] += A[i][j]
    
cnt = 0
for i in range(n):
    for j in range(n):
        if len(ground[i][j]) > 0:
            cnt += len(ground[i][j])

print(cnt)