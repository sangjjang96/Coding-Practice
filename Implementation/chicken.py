import sys

N, M = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

mini = int(1e9)

home = []
store = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            home.append([i+1, j+1])
        elif maps[i][j] == 2:
            store.append([i+1, j+1])

visited = [False] * len(store)


def dfs(idx, cnt):
    global mini
    
    if cnt == M:
        answer = 0
        
        for i in home:
            distance = int(1e9)
            for j in range(len(visited)):
                if visited[j]:
                    ran = abs(i[0] - store[j][0]) + abs(i[1] - store[j][1])
                    distance = min(distance, ran)
            answer += distance
        mini = min(answer, mini)
        return
    
    for i in range(idx, len(store)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, cnt+1)
            visited[i] = False
    
dfs(0, 0)

print(mini)