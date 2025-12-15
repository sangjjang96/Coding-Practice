import sys
import heapq

n, m = list(map(int, sys.stdin.readline().split()))

graphs = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    graphs[a].append((b, c))
    graphs[b].append((a, c))
    

start, end = list(map(int, sys.stdin.readline().split()))

distances = [0] * (n+1)

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (-int(1e9), start))
    distances[start] = int(1e9)
    
    while q:
        dist, now = heapq.heappop(q)
        
        dist = -dist
        if distances[now] > dist:
            continue
        
        for i in graphs[now]:
            cost = min(dist, i[1])
            
            if cost > distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (-cost, i[0]))

dijkstra(start)

print(distances[end])