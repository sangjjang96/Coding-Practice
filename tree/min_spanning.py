import sys
sys.setrecursionlimit(100000)

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

v, e = list(map(int, sys.stdin.readline().split()))

routes = []

parents = [0]*(v+1)

for i in range(v+1):
    parents[i] = i

for _ in range(e):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    routes.append([c, a, b])

routes.sort()

ans = 0
for c, a, b in routes:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += c

print(ans)