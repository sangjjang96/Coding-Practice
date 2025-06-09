import sys
import heapq

n = int(input())

works = []
max_day = 0

for _ in range(n):
    d, w = list(map(int, sys.stdin.readline().split()))
    
    heapq.heappush(works, (-w, d))
    
    if max_day < d:
        max_day = d
        
days = [False] * (max_day+1)

ans = 0

while works:
    w, d = heapq.heappop(works)
    
    w = -w
    
    for i in range(d, 0, -1):
        if days[i]:
            continue
        
        days[i] = True
        ans += w
        break
    
print(ans)