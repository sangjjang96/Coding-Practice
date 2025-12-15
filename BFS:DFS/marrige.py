import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graphs = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    graphs[a].append(b)
    graphs[b].append(a)

visit = [0]*(n+1)
cand = graphs[1]

for c in cand:
    visit[c] = 1

for c in cand:
    for g in graphs[c]:
        visit[g] = 1

visit[1] = 0
print(sum(visit))