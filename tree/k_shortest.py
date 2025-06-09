import sys
import heapq

n, m, k = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    graph[a].append([b, c])

distances = [[] for _ in range(n+1)]

distances[0].append(-1)
for i in range(1, n+1):
    distances[i].append(int(1e9))

def dijkstra(start):
    q = []
    
    heapq.heappush(q, [0, start])
    distances[start].append(0)
    
    while q:
        dist, now = heapq.heappop(q)

        if min(distances[now]) < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < max(distances[i[0]]):
                distances[i[0]].append(cost)
                heapq.heappush(q, (cost, i[0]))
            
dijkstra(1)

for dist in distances[1:]:
    dist.sort()
    if len(dist) < k or dist[k-1] == int(1e9):
        print(-1)
    else:
        print(dist[k-1])