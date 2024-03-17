def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    
    for i in graph[start]:
        if visited[i] != True:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,7],
    [1,4,6],
    [1,5,7],
    [2,6],
    [3,7],
    [2,4],
    [1,3]
]

visited = [False] * 9

dfs(graph, 1, visited)