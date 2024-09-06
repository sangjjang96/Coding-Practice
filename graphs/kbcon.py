import sys

inf = int(1e9)

N, M = list(map(int, sys.stdin.readline().split()))

rel = [[inf]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            rel[i][j] = 0

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    rel[a][b] = 1
    rel[b][a] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            rel[a][b] = min(rel[a][b], rel[a][k] + rel[k][b])

sums = []

for r in rel[1:]:
    sums.append(sum(r[1:]))

print(sums.index(min(sums))+1)