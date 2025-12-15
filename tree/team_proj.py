import sys
sys.setrecursionlimit(10**6)

t = int(input())

def bfs(start):
    global cnt
    
    visited[start] = 1
    nxt = selections[start]
    
    if not visited[nxt]:
        bfs(nxt)
    elif not done[nxt]:
        j = nxt
        while j != start:
            cnt += 1
            j = selections[j]
        cnt += 1
    
    done[start] = 1

for _ in range(t):
    n = int(input())
    
    selections = [0] + list(map(int, sys.stdin.readline().split()))
    
    visited = [0]*(n+1)
    done = [0]*(n+1)
    
    cnt = 0
    
    for idx in range(1, n+1):
        if not visited[idx]:
            bfs(idx)
    
    print(n-cnt)