import sys
import heapq

t = int(input())

for _ in range(t):
    n, d, c = list(map(int, sys.stdin.readline().split()))
    
    distances = [int(1e9)] * (n+1)
    
    connections = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = list(map(int, sys.stdin.readline().split()))

        connections[b].append([a, s])
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, [0, start])
        distances[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distances[now] < dist:
                continue
            for i in connections[now]:
                cost = dist + i[1]
                if cost < distances[i[0]]:
                    distances[i[0]] = cost
                    heapq.heappush(q, [cost, i[0]])
    
    dijkstra(c)
    
    num = 0
    ans = 0
    
    for distance in distances:
        if distance != int(1e9):
            num += 1
            ans = max(ans, distance)
    
    print(num, ans)