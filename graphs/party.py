import sys
import heapq

N, M, X = list(map(int, sys.stdin.readline().split()))

roads = [[] for _ in range(N+1)]

inf = int(1e9)
distance = [[inf]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, t = list(map(int, sys.stdin.readline().split()))
    roads[a].append([b, t])

def dij():
    for i in range(1, N+1):
        q = []
        heapq.heappush(q, [0, i])
        distance[i][i] = 0
        
        while q:
            dist, node = heapq.heappop(q)
            
            if distance[i][node] < dist:
                continue
            
            for next in roads[node]:
                cost = distance[i][node] + next[1]
                
                if cost < distance[i][next[0]]:
                    distance[i][next[0]] = cost
                    heapq.heappush(q, [cost, next[0]])

dij()

times = []
for i in range(1, N+1):
    time = distance[i][X] + distance[X][i]
    times.append(time)

print(max(times))