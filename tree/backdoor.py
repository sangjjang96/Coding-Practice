import sys
import heapq

n, m = list(map(int, sys.stdin.readline().split()))

sight = list(map(int, sys.stdin.readline().split()))

junctions = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    junctions[a].append((b, c))
    junctions[b].append((a, c))
    
distances = [float('inf')] * (n+1)

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distances[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if sight[now] and now != n-1:
            continue
        
        if distances[now] < dist:
            continue
        
        for i in junctions[now]:
            cost = dist + i[1]
            
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)

if distances[n-1] != float('inf'):
    print(distances[n-1])
else:
    print(-1)
    