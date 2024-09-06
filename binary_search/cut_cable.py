import sys

K, N = list(map(int, sys.stdin.readline().split()))

cables = []

for _ in range(K):
    cables.append(int(sys.stdin.readline()))


start, end = 1, max(cables)

while start <= end:
    mid = (start + end) // 2
    
    summ = 0
    
    for c in cables:
        summ += (c // mid)
    
    if summ >= N:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)