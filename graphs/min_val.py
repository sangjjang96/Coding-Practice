import sys
import heapq

N = int(input())
M = int(input())

route = [[] for _ in range(N+1)]

inf = int(1e9)
distance = [inf] * (N+1)

for _ in range(M):
    a, b, v = list(map(int, sys.stdin.readline().split()))
    
    route[a].append([b, v])
    
start, end = list(map(int, sys.stdin.readline().split()))

def dij(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue
        
        for next in route[node]:
            cost = distance[node] + next[1]
            
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, [cost, next[0]])

dij(start)

print(distance[end])    