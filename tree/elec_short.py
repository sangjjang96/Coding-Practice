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

while True:
    m, n = list(map(int, sys.stdin.readline().split()))
    
    if [m, n] == [0, 0]:
        break

    parents = [0]*m
    roads = []
    
    for i in range(m):
        parents[i] = i

    total_elec = 0
    for i in range(n):
        a, b, c = list(map(int, sys.stdin.readline().split()))
        total_elec += c
        roads.append([c, a, b])

    roads.sort()

    selected = []
    optimal_elec = 0
    for c, a, b in roads:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            optimal_elec += c
            selected.append(c)

    print(total_elec - optimal_elec)    