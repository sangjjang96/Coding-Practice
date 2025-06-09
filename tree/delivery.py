import sys
import heapq

n, m = list(map(int, sys.stdin.readline().split()))

routes = [[] for _ in range(n+1)]

distances = [int(1e9)] * (n+1)

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    routes[a].append([b, c])
    routes[b].append([a, c])

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distances[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in routes[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    
dijkstra(1)

print(distances[n])
