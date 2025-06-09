import sys
sys.setrecursionlimit(1000000)

n = int(input())

trees = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    trees[a].append([b, c])
    trees[b].append([a, c])
    
def dfs(x, dist):
    for i in trees[x]:
        if distances[i[0]] == -1:
            distances[i[0]] = dist + i[1]
            dfs(i[0], dist + i[1])

distances = [-1] * (n+1)         
distances[1] = 0
dfs(1, 0)

start = distances.index(max(distances))
distances = [-1] * (n+1)
distances[start] = 0
dfs(start, 0)

print(max(distances))