import sys
from collections import deque

a, b = list(map(int, sys.stdin.readline().split()))

mem = {}

def bfs():
    q = deque([])
    q.append([a, 0])
    
    while q:
        x, steps = q.popleft()
        
        for i in [2*x, int(str(x)+'1')]:
            steps_ = steps + 1
            if i <= b:
                if i == b:
                    return steps_
                else:                
                    q.append([i, steps_])

answer = bfs()

if answer:
    print(answer+1)
else:
    print(-1)