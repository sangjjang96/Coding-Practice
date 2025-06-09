import sys
import math
from collections import deque

n, m, k = list(map(int, sys.stdin.readline().split()))

fireballs = []
for _ in range(m):
    r, c, m, s, d = list(map(int, sys.stdin.readline().split()))
    
    fireballs.append([r-1, c-1, m, s, d])

chessboard = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    # Direction 1
    while fireballs:
        r_cur, c_cur, m_cur, s_cur, d_cur = fireballs.pop(0)
        r_new = (r_cur + s_cur * dx[d_cur]) % n
        c_new = (c_cur + s_cur * dy[d_cur]) % n
        chessboard[r_new][c_new].append([m_cur, s_cur, d_cur])
    
    # Direction 2
    for i in range(n):
        for j in range(n):
            if len(chessboard[i][j]) > 1 :
                m_sum, s_sum, odd, even, cnt = 0, 0, 0, 0, len(chessboard[i][j])
                
                while chessboard[i][j]:
                    m, s, d = chessboard[i][j].pop(0)
                    m_sum += m
                    s_sum += s
                    
                    if d % 2:
                        odd += 1
                    else:
                        even += 1
                    
                if odd == cnt or even == cnt:
                    direction = [0, 2, 4, 6]
                else:
                    direction = [1, 3, 5, 7]
                
                if m_sum // 5:
                    for dir in direction:
                        fireballs.append([i, j, m_sum//5, s_sum//cnt, dir])

            if len(chessboard[i][j]) == 1:
                fireballs.append([i, j] + chessboard[i][j].pop())

print(sum([f[2] for f in fireballs]))