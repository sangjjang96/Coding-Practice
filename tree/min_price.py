import sys
import heapq

n = int(input())

m = int(input())

buses = [[] for _ in range(n+1)]
distances = [int(1e9)] * (n+1)

routes = [0] * (n+1)

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().rstrip().split()))
    
    buses[a].append([b, c])
    
start, end = list(map(int, sys.stdin.readline().rstrip().split()))

def dijkstra(s):
    q = []
    
    heapq.heappush(q, (0, s))
    distances[s] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in buses[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                routes[i[0]] = now
                heapq.heappush(q, (cost, i[0]))
    
dijkstra(start)

print(distances[end])

path = [end]
now = end
while now != start:
    now = routes[now]
    path.append(now)
path.reverse()

print(len(path))
print(' '.join(map(str, path)))