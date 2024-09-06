import sys

N, M = list(map(int, sys.stdin.readline().split()))

heights = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(heights)

while start <= end:
    mid = (start+end) // 2
    
    summ = 0
    for i in heights:
        if i >= mid:
            summ += i - mid   
    
    if summ >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)