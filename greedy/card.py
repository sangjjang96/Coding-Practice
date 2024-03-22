import sys
import heapq

N = int(input())

cards = []

for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

total = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum = a + b
    
    total += sum
    heapq.heappush(cards, sum)

print(total)