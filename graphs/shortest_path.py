import sys
import heapq

V, E = list(map(int, sys.stdin.readline().split()))

K = int(sys.stdin.readline())

inf = int(1e9)
distance = [inf]*(V+1)

paths = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    
    paths[u].append([v, w])

def dij(start):
    q = []
    heapq.heappush(q, [0, K])
    distance[K] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue
        
        for next in paths[node]:
            cost = distance[node] + next[1]
            
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                q.append([cost, next[0]])

dij(K)

for i in range(1, V+1):
    if i == K:
        print(0)
    else:
        dis = distance[i]
        
        if dis == inf:
            print('INF')
        else:
            print(dis)