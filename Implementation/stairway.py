import sys

ans = 0

n, l = list(map(int, sys.stdin.readline().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def check_route(road):
    global n, l
    visited = [0]*n
    
    for i in range(n-1):
        if road[i] != road[i+1]:
            if abs(road[i] - road[i+1]) > 1:
                return False
            else:
                if road[i] - road[i+1] == 1:
                    if i + 1 + l > n:
                        return False
                    check = road[i+1]
                    for j in range(i+1, i+1+l):
                        if visited[j] or road[j] != check:
                            return False
                        visited[j] = 1
                elif road[i] - road[i+1] == -1:
                    if i - l < -1:
                        return False
                    check = road[i]
                    for j in range(i, i-l, -1):
                        if visited[j] or road[j] != check:
                            return False
                        visited[j] = 1
    return True

for r in maps:
    if check_route(r):
        ans += 1
    
for c in range(n):
    if check_route([maps[r][c] for r in range(n)]):
        ans += 1

print(ans)