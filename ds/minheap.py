import sys
import heapq

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    inp = int(sys.stdin.readline())
    
    if inp == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, inp)