import sys

ans = 0

n, l = list(map(int, sys.stdin.readline().rstrip().split()))

pos = list(map(int, sys.stdin.readline().rstrip().split()))

done = [-1]*(1001)

pos.sort()

for p in pos:
    if done[p] >= 0:
        continue
    
    for i in range(p, p+l):
        if i <= 1000:
            done[i] += 1
    ans += 1

print(ans)