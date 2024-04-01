import heapq
import sys
input = sys.stdin.readline

N = int(input())

ST = []

for _ in range(N):
    ST.append(list(map(int, input().split(' '))))
ST.sort(key=lambda x : (x[0], x[1]))

ends = [ST[0][1]]

for i in range(1, N):
    if ends[0] <= ST[i][0]:
        heapq.heappop(ends)
    heapq.heappush(ends, ST[i][0])
    
print(len(ends))