import sys
from collections import deque
from itertools import *

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, d = list(map(int, sys.stdin.readline().split()))

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cands = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cands.append([i, j])

poses = list(combinations(cands, 3))

def bfs(pos):
    q = deque()
    q.append(pos)
    
    