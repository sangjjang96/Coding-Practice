N, M = map(int,input().split())

graph = []

for i in range(1):
    graph.append([0]*N)

for i in range(1, M+1):
    graph.append(list(map(int, input().split())))

print(graph)