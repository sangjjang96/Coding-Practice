import sys
from collections import deque

INF = 100001

n, k = list(map(int, sys.stdin.readline().split()))

visited = [0]*INF
visited_ = [0]*INF

def bfs(x):
    q = deque()
    q.append(x)
    
    while q:
        x_ = q.popleft()
        
        for nx in [x_-1, x_+1, 2*x_]:
            if 0 <= nx < INF and not visited[nx]:
                visited[nx] = visited[x_] + 1
                q.append(nx)

cnt = 0
def bfs_(x):
    global cnt
    
    q = deque()
    q.append(x)
    
    while q:
        x_ = q.popleft()
        
        if x_ == k and visited_[x_] == visited[k]:
            cnt += 1
        
        for nx in [x_-1, x_+1, 2*x_]:
            if 0 <= nx < INF and not visited_[nx]:
                visited_[nx] = visited_[x_] + 1
                    
                q.append(nx)

bfs(n)
bfs_(n)

print(visited[k])
print(cnt)