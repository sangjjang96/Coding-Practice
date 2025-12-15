import sys

n, m = list(map(int, sys.stdin.readline().split()))

dist = [int(1e9)]*(n+1)

graphs = []

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    graphs.append([a, b, c])

dist[1] = 0

for i in range(n):
    for j in range(m):
        cur, nxt, cst = graphs[j]
        
        if dist[cur] != int(1e9) and dist[nxt] > dist[cur] + cst:
            dist[nxt] = dist[cur] + cst
            
            if i == n-1:
                print(-1)
                exit()

for i in range(2, n+1):
    if dist[i] == int(1e9):
        print(-1)
    else:
        print(dist[i])
