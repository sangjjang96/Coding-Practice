import sys
import heapq
import math

t = int(sys.stdin.readline())

for _ in range(t):
    left = []
    right = []
    
    m = int(sys.stdin.readline())
    
    nums = []
    
    todo = math.ceil(m / 10)
    
    for _ in range(todo):
        tmp = list(map(int, sys.stdin.readline().split()))
        
        nums.extend(tmp)
    
    cnt = m//2 if m % 2 == 0 else m//2 + 1

    print(cnt)
    
    ten = 0
    for idx, n in enumerate(nums):
        if len(left) == len(right):
            heapq.heappush(left, -n)
        else:
            heapq.heappush(right, n)
            
        if right and right[0] < -left[0]:
            l = heapq.heappop(left)
            r = heapq.heappop(right)
            
            heapq.heappush(left, -r)
            heapq.heappush(right, -l)

        if (idx+1) % 2 != 0:
            print(-left[0], end=' ')
            ten += 1
        
        if ten == 10:
            print()
            ten = 0