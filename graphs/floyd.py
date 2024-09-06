import sys

inf = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

relations = [[inf]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            relations[i][j] = 0

for _ in range(m):
    a, b, v = list(map(int, sys.stdin.readline().split()))
    
    relations[a][b] = min(relations[a][b], v)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            relations[a][b] = min(relations[a][b], relations[a][k] + relations[k][b])


for rel in relations[1:]:
    for r in rel[1:]:
        if r == inf:
            r = 0
        print(r, end=' ')
    print()