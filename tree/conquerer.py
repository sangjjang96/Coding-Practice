import sys
import heapq

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    
    return parents[x]

def union_parents(a, b):
    a = find_parents(a)
    b = find_parents(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n, m, t = list(map(int, sys.stdin.readline().split()))

roads = []
conquered = []

ans = (n-2)*(n-1)*t//2
for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(roads, (c, a, b))

parents = [0]*(n+1)

for i in range(n+1):
    parents[i] = i

i = 0
while i < n-1:
    c, a, b = heapq.heappop(roads)
    
    if find_parents(a) != find_parents(b):
        union_parents(a, b)
        ans += c
        i += 1

print(ans)