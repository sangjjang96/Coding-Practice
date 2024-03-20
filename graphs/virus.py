N = int(input())
M = int(input())

V = 1

graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0]*(N+1)
answer = []

def dfs(V):
    visited1[V] = 1 #방문처리
    answer.append(V)
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)
            
dfs(V)

print(len(answer)-1)