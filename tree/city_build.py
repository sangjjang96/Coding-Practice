import sys

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]
    
    
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    
    
n, m = list(map(int, sys.stdin.readline().split()))

roads = []

ans = 0
for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    roads.append((c, a, b))
    ans += c

roads.sort()

parents = [0] * (n+1)

for i in range(n+1):
    parents[i] = i

for c, a, b in roads:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans -= c

cnt = 0
for i in range(1, n):
    if i == parents[i]:
        cnt += 1

if cnt > 1:
    print(-1)
else:
    print(ans)
