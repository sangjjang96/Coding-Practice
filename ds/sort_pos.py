import sys
import heapq

n = int(input())

pos = []
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    
    heapq.heappush(pos, [x, y])

while pos:
    print(*heapq.heappop(pos))