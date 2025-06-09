import sys
import heapq

t = int(input())
    

for _ in range(t):
    def dijkstra(start):
        q = []
        
        distances = [int(1e9)]*(n+1)
        
        heapq.heappush(q, (0, start))
        distances[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distances[now] < dist:
                continue
            for i in roads[now]:
                cost = dist + i[1]
                if cost < distances[i[0]]:
                    distances[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distances
    
    n, m, t = list(map(int, sys.stdin.readline().split()))
    s, g, h = list(map(int, sys.stdin.readline().split()))
    
    roads = [[] for _ in range(n+1)]
    
    destinations = []
    
    for _ in range(m):
        a, b, d = list(map(int, sys.stdin.readline().split()))
        
        if (a == g and b == h) or (b == g and a == h):
            g2h = d
        
        roads[a].append([b, d])
        roads[b].append([a, d])
    
    for _ in range(t):
        x = int(sys.stdin.readline())
        
        destinations.append(x)
    
    from_s = dijkstra(s)
    from_g = dijkstra(g)
    from_h = dijkstra(h)
    
    ans = []
    
    for destin in destinations:        
        if (from_s[g] + g2h + from_h[destin] == from_s[destin]) or (from_s[h] + g2h + from_g[destin] == from_s[destin]):
            ans.append(destin)
    
    ans.sort()
    print(*ans)