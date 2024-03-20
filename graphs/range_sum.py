N, M = list(map(int, input().split()))

graph = []
x1s = []
y1s = []
x2s = []
y2s = []

answers = []

for i in range(N):
    g = list(map(int, input().split()))
    graph.append(g)

for i in range(M):
    x1, y1, x2, y2 = list(map(int,input().split()))
    x1s.append(x1-1)
    y1s.append(y1-1)
    x2s.append(x2-1)
    y2s.append(y2-1)

for i in range(M):
    sum = 0
    for j in range(x1s[i], x2s[i]+1):
        for k in range(y1s[i], y2s[i]+1):
            sum += graph[j][k]  
    answers.append(sum)
    sum = 0

for a in answers:
    print(a)