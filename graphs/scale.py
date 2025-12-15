import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graphs = [[int(1e9)]*(n+1) for _ in range(n+1)]
results = [0]*(n+1)

for i in range(n+1):
    graphs[i][i] = 1
    
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    graphs[a][b] = 1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            graphs[i][j] = min(graphs[i][j], graphs[i][k] + graphs[k][j])
            

for i in range(1, n+1):
    for j in range(1, n+1):
        if graphs[i][j] == int(1e9) and graphs[j][i] == int(1e9):
            results[i] += 1

for r in results[1:]:
    print(r)