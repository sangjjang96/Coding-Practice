import sys
import heapq

n, m = list(map(int, sys.stdin.readline().split()))

lines = [[] for _ in range(n+1)]
distances = [int(1e9)]*(n+1)

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    lines[a].append((b, c))
    lines[b].append((a, c))

prev = [0]*(n+1)
def djikstra(start):
    global distances
    
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distances[now] < dist:
            continue
        
        for i in lines[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                prev[i[0]] = now
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

djikstra(1)
print(n-1)
for i in range(2, n+1):
    print(i, prev[i])