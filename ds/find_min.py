import sys
from collections import deque

n, l = list(map(int, sys.stdin.readline().split()))

nums = list(map(int, sys.stdin.readline().split()))

q = deque([])

for i in range(n):
    if q and q[0][0] <= i-l:
        q.popleft()
        
    while len(q) >= 1 and nums[i] < q[-1][1]:
        q.pop()
    
    q.append((i, nums[i]))

    print(q[0][1], end=' ')