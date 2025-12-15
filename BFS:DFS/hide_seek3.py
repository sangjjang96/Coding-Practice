import sys
import heapq

n, k = list(map(int, sys.stdin.readline().split()))

t = 0
if n == k:
    print(0)
else:
    heap = []
    dic = {}
    
    if n == 0:
        n += 1
        t += 1
        dic[0] = 0
    
    dic[n] = t
    
    heapq.heappush(heap, (t, n))
    
    while heap:
        t, x = heapq.heappop(heap)
        
        if x == k:
            print(t)
            break
        
        for i in (x+1, x-1, 2*x):
            if 0 <= i <= 100000:
                t_ = t + (i != 2*x)
                
                if i not in dic or t_ < dic[i]:
                    dic[i] = t_
                    heapq.heappush(heap, (t_, i))