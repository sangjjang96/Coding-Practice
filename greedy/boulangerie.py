import sys

from collections import deque

dx = [1, 1, 1]
dy = [-1, 0, 1]

r, c = list(map(int, sys.stdin.readline().split()))

maps = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]

roads = []

for map in maps:
    tmp = []
    
    for m in map:
        if m == '.':
            tmp.append(0)
        else:
            tmp.append(1)

    roads.append(tmp)

for road in roads:
    print(road)