import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, sys.stdin.readline().rstrip().split())
maps = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

visited = [[-1]*c for _ in range(r)]

q = deque()

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'D':
            end = (i, j)
            maps[i][j] = '.'
        elif maps[i][j] == 'S':
            start = (i, j)
            maps[i][j] = '.'

# print(start, end)

def bfs():
    global start, end
    
    x_end, y_end = end
    
    ans = 0
    
    q = deque()
    visited = [[0]*c for _ in range(r)]
    
    i, j = start
    
    q.append((i, j))
    visited[i][j] = 1
    
    while q:
        # 시작 지점 넣고 거기서부터 시작
        for _ in range(len(q)):
            i, j = q.popleft()
            
            for k in range(4):
                i_, j_ = i + dx[k], j + dy[k]
                
                # 범위 내인지 확인
                if not (0 <= i_ < r and 0 <= j_ < c):
                    continue
                
                # 방문한 적 없고 빈 공간이면 방문
                if visited[i_][j_] == 0 and maps[i_][j_] == '.':
                    
                    # 비버 굴이면 거리 출력
                    if i_ == x_end and j_ == y_end:
                        return ans + 1
                    
                    # 주변에 물이 다음번에 이 위치에 도달한다면 0
                    # 상관 없으면 1
                    flag = 1
                    for k_ in range(4):
                        i__, j__ = i_ + dx[k_], j_ + dy[k_]
                        if not (0 <= i__ < r and 0 <= j__ < c):
                            continue
                        if maps[i__][j__] == '*':
                            flag = 0
                    
                    # 안전한 공간이면 그 위치로 방문
                    if flag:
                        q.append((i_, j_))
                        visited[i_][j_] = 1
        
        # 모든 물에 대해 가능한 방향에 대해 퍼지도록 만들기
        water = []
        for i in range(r):
            for j in range(c):
                if maps[i][j] == '*':
                    for k in range(4):
                        i_, j_ = i + dx[k], j + dy[k]
                        
                        if not (0 <= i_ < r and 0 <= j_ < c):
                            continue
                        
                        if i_ == x_end and j_ == y_end:
                            continue
                        
                        if maps[i_][j_] == '.':
                            water.append((i_, j_))
        
        for x, y in water:
            maps[x][y] = '*'
        
        # 턴 하나 증가
        ans += 1
    
    return 'KAKTUS'


print(bfs())