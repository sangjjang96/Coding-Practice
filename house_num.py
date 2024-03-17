import sys

N = M = int(input())

#행렬 만들기
graph = [[]*(N+1) for _ in range(N+1)]
for i in range (M):
    house = input()
    for idx, h in enumerate(house):
        if h == '1':
            graph[i].append(idx+1)
            graph[idx+1].append(i)

visited = [False]*(N+1)

from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    # print(start, end=' ')
    
    for i in graph[start]:
        if visited[i] != True:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    q = deque([start])
    
    visited[start] = True
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
num = 0
for i in range(1, N+1):
    if visited[i] != True:
        # dfs(graph, i, visited)
        bfs(graph, i, visited)
        num += 1

print(graph)
        
print(num)