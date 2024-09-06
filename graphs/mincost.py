import heapq
import sys

inf = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

relation = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, v = list(map(int, sys.stdin.readline().split()))
    
    relation[a].append([b, v])

f, t = list(map(int, sys.stdin.readline().split()))

distance = [inf]*(N+1)
q = [[0, f]]
distance[f] = 0

while q:
    now_v, now_b = heapq.heappop(q)
    
    if now_v > distance[now_b]:
        continue
    
    else:
        for next_b, next_v in relation[now_b]:
            dist = next_v + now_v
            
            if distance[next_b] > dist:
                distance[next_b] = dist
                heapq.heappush(q, [dist, next_b])

print(distance[t])