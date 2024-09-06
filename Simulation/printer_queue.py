import sys
import heapq

T = int(sys.stdin.readline())

N, M = list(map(int, sys.stdin.readline().split()))

script = list(map(int, sys.stdin.readline().split()))

obj = script[M]

q = []

for s in script:
    heapq.heappush(q, (-s, s))

print(q)

out = []

while q:
    out.append(heapq.heappop(q))

for i in range(len(out)):
    if out[i][1] == 