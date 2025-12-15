import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())

def bfs(x, y, maps):
    q = deque(())
    

for _ in range(T):
    w, h = list(map(int, sys.stdin.readline().split()))
    
    fires = []
    exits = []
    maps = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '.':
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    exits.append((i, j))
                    
                maps[i][j] = 0
            elif maps[i][j] == '#':
                maps[i][j] = 1
            elif maps[i][j] == '@':
                maps[i][j] = 0
                start_x, start_y = i, j
            elif maps[i][j] == '*':
                maps[i][j] = 1
                fires.append((i, j))
    
    for m in maps:
        print(m)
    
    print(fires)
    print(exits)