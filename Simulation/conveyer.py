import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))

a = list(map(int, sys.stdin.readline().split()))
a = deque(a)

robots = deque([])
cnt = 0
while True:
    print(a, a.count(0))
    if a.count(0) == k:
        break
    
    if a[0] > 0:
        if len(robots) < n:
            robots.append(0)
    
    for i in range(len(robots)):
        if robots[i] == (n-1):
            if a[robots[i]] > 0:
        if a[robots[i]] > 0:
            a[robots[i]] -= 1
            robots[i] += 1
            robots[i] %= (2*n)
    
    tmp = a.pop()
    a.appendleftt(tmp)
    
    cnt += 1
    
print(cnt-1)