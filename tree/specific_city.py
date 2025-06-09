import sys
import heapq

n, m, k, x = list(map(int, sys.stdin.readline().split()))

routes = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    routes[a].append([b, 1])

distances = [int(1e9)] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distances[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
            
        if distances[now] < dist:
            continue
        for i in routes[now]:
            distance = dist + i[1]
            if distance < distances[i[0]]:
                distances[i[0]] = distance
                heapq.heappush(q, [distance, i[0]])
            
                

dijkstra(x)

if k not in distances:
    print(-1)
else:
    for idx, dist in enumerate(distances):
        if dist == k:
            print(idx)