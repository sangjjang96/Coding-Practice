from collections import deque

N, K = list(map(int, input().split()))

def bfs():
    q = deque([])
    q.append(N)
    
    while q:
        x_ = q.popleft()
        
        if x_ == K:
            print(dist[x_])
            break
        for nx in (x_-1, x_+1, 2*x_):
            if 0 <= nx < INF and not dist[nx]: 
                dist[nx] = dist[x_]+1
                q.append(nx)

INF = 100001
dist = [0]*INF

bfs()