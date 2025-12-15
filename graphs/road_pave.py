import sys
import heapq

n, m, k = list(map(int, sys.stdin.readline().split()))

roads = [[] for _ in range(n+1)]
prev = [0]*(n+1)
distances = [[int(1e12)]*(n+1) for _ in range(k+1)]

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    roads[a].append((b, c))
    roads[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, 0))
    for i in range(k+1):
        distances[i][start] = 0
    
    
    while q:
        dist, now, now_k = heapq.heappop(q)
        
        if distances[now_k][now] < dist:
            continue
        
        for i in roads[now]:
            cost = dist + i[1]
            
            if cost < distances[now_k][i[0]]:
                distances[now_k][i[0]] = cost
                heapq.heappush(q, (cost, i[0], now_k))
            if now_k < k:
                if dist < distances[now_k+1][i[0]]:
                    distances[now_k+1][i[0]] = dist
                    heapq.heappush(q, (dist, i[0], now_k+1))

dijkstra(1)

ans = int(1e12)
for i in range(k+1):
    ans = min(ans, distances[i][n])
print(ans)