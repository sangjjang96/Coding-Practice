import sys
import heapq

n = int(sys.stdin.readline())

q_l = []
q_r = []

for _ in range(n):
    said = int(sys.stdin.readline())
    
    # 왼쪽 오른쪽에 번갈아 넣어줌
    if len(q_l) == len(q_r):
        heapq.heappush(q_l, -said)
    else:
        heapq.heappush(q_r, said)
    
    # right가 left보다 큰 경우 right와 left를 교체한다.
    if q_r and q_r[0] < -q_l[0]:
        left = heapq.heappop(q_l)
        right = heapq.heappop(q_r)
        
        heapq.heappush(q_l, -right)
        heapq.heappush(q_r, -left)
    
    print(-q_l[0])