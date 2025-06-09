import sys

n, m = list(map(int, sys.stdin.readline().split()))

relations = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = list(map(int, sys.stdin.readline().split()))
    
    relations[u].append(v)
    relations[v].append(u)
    
