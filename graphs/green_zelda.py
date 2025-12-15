import sys
import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

idx = 1
while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
    
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    heap = []
    
    lupis = [[int(1e9)] * n for _ in range(n)]
    
    lupis[0][0] = maps[0][0]
    
    heapq.heappush(heap, (maps[0][0], 0, 0))
    
    while heap:
        dist, x, y = heapq.heappop(heap)
        
        if [x, y] == [n-1, n-1]:
            print(f'Problem {idx}: {dist}')
            break
        
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            
            if 0 <= x_ < n and  0 <= y_ < n:
                cost = dist + maps[x_][y_]
                
                if cost < lupis[x_][y_]:
                    lupis[x_][y_] = dist + maps[x_][y_]
                    heapq.heappush(heap, (dist + maps[x_][y_], x_, y_))
    
    idx += 1