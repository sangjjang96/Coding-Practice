import sys
import heapq

inf = int(1e9)
ans = 0

N, E = list(map(int, sys.stdin.readline().split()))

relations = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, v = list(map(int, sys.stdin.readline().split()))
    
    relations[a].append([b, v])
    relations[b].append([a, v])
    
def dij(start):
    distance = [inf]*(N+1)
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    
    while q:
        now_cost, now = heapq.heappop(q)
        
        if distance[now] < now_cost:                # 현재 거리가 더 짧으면 넘김
            continue
        
        for i in relations[now]:                    # 현재 시작점과 연결된 간선내에서
            cost = now_cost + i[1]                  # 이전까지 거리 + 다음 노드까지 거리
            
            if distance[i[0]] > cost:               # 기존 저장거리보다 위에서 계산한 거리가 짧을 때
                distance[i[0]] = cost               # 갱신
                heapq.heappush(q, [cost, i[0]])     # 다음 노드 heapq에 넣기
                
    return distance

v1, v2 = list(map(int, sys.stdin.readline().split()))

dis = dij(1)
dis_v1 = dij(v1)
dis_v2 = dij(v2)


ans = min(dis[v1] + dis_v1[v2] + dis_v2[v], dis[v2] + dis_v2[v1] + dis_v1[v])
if ans >= inf:
    ans = -1

print(ans)