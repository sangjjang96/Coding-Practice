import sys
import heapq

n, d = list(map(int, sys.stdin.readline().split()))

highways = [[] for _ in range(d+1)]

poses = []

for _ in range(n):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    
    highways[a].append((b, c))
    
    if a not in poses:
        poses.append(a)
    if b not in poses:
        poses.append(b)

distances = [int(1e9)] * (d+1)
def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distances[now] < dist:
            continue
        
        for i in highways[now]:
            if i[0] > d:
                continue
            cost = dist + i[1]
            
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)

for pose in poses:
    if pose < d+1:
        print(pose, distances[pose])