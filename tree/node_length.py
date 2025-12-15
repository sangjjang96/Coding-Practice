import sys
import heapq

n, m = list(map(int, sys.stdin.readline().split()))

graphs = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    graphs[a].append((b, c))
    graphs[b].append((a, c))
    

def dijkstra(start):
    distances = [int(1e9)]*(n+1)
    
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distances[now] < dist:
            continue
        
        for i in graphs[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distances

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    dist = dijkstra(a)
    
    print(dist[b])