import sys

def dfs(start):
    visited[start] = 1
    
    print(start, end=' ')
    
    for i in nodes[start]:
        if not visited[i]:
            dfs(i)
            

visited = [0] * 8

nodes = [
    [],
    [2, 3, 7],
    [4, 6],
    [1, 5, 7],
    [2, 6],
    [3],
    [2, 4],
    [1, 3],
]

dfs(1)