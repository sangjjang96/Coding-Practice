import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(N+1)]
lines = []

for _ in range(M):
    a, b, v = list(map(int, sys.stdin.readline().split()))
    lines.append((v, a, b))

lines.sort()
result = 0
for c, a, b in lines:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += c

print(result)