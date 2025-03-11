import sys
import heapq

n, k = list(map(int, sys.stdin.readline().split()))

jewels = []

for _ in range(n):
    heapq.heappush(jewels, list(map(int, sys.stdin.readline().split())))

bags = []

for _ in range(k):
    c = int(input())
    bags.append(c)
bags.sort()

answer = 0
cand = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(cand, -heapq.heappop(jewels)[1])

    if cand:
        answer -= heapq.heappop(cand)
    elif not jewels:
        break
    
print(answer)