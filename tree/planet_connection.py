import sys
sys.setrecursionlimit(100000)

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
        

n = int(input())

parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

flows = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

flows_l = []

for i in range(n):
    for j in range(i+1, n):
        flows_l.append([flows[i][j], i, j])

flows_l.sort()

ans = 0
for c, a, b in flows_l:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += c

print(ans)