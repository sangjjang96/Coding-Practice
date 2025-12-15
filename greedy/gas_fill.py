import sys
import heapq

ans = 0
n = int(sys.stdin.readline())

services = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
l, p = list(map(int, sys.stdin.readline().split()))

services.append([l, 0])
services.sort()

q = []

# 하나씩 다니면서 정보를 q에 넣기
# 다니다가 기름 부족하면 q에 있는 정보를 기반으로 가장 큰 기름 양을 가진 곳에서 채움
# 반복하면서 끝까지 가면 끝
for i in range(len(services)):
    if p - services[i][0] < 0:
        while q:
            p += -heapq.heappop(q)
            ans += 1
            if p - services[i][0] >= 0:
                break
    if len(q) == 0 and p - services[i][0] < 0:
        ans = -1
        break
    else:
        heapq.heappush(q, -services[i][1])

print(ans) 
            