import sys
import heapq

n = int(input())

m = int(input())

roads = [[] for _ in range(n)]

for i in range(n):
    connections = list(map(int, sys.stdin.readline().split()))
    
    for j in range(i+1, n):
        if connections[j] == 1:
            roads[i].append((j, 1))
            roads[j].append((i, 1))
    
plan = list(map(int, sys.stdin.readline().split()))

def dijkstra(start):
    distances = [int(1e9)]*(n+1)
    
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distances[now]:
            continue
        for i in roads[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distances

ans = 'YES'

for i in range(len(plan)-1):
    result = dijkstra(plan[i]-1)
    
    if result[plan[i+1]-1] == int(1e9):
        ans = 'NO'
        break

print(ans)