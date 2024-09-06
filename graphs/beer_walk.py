import sys
from collections import deque

t = int(input())

def bfs():    
    while q:
        x, y = q.popleft()
        
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            print('happy')
            return
        
        for i in range(n):
            if not visited[i]:
                x_, y_ = conv[i]
                if abs(x - x_) + abs(y - y_) <= 1000:
                    visited[i] = 1
                    q.append([x_, y_])
        
    print('sad')
    return
        

for i in range(t):
    q = deque([])
    
    n = int(input())
    
    home = list(map(int, sys.stdin.readline().split()))
    q.append(home)
    
    conv = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    festival = list(map(int, sys.stdin.readline().split()))
    
    visited = [0 for _ in range(n+1)]
    
    bfs()