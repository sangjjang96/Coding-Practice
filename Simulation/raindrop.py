import sys

ans = 0

H, W = list(map(int, sys.stdin.readline().split()))

blocks = list(map(int, sys.stdin.readline().split()))

ans = 0

for i in range(1, W-1):
    l_max = max(blocks[:i])
    r_max = max(blocks[i+1:])
    
    cmp = min(l_max, r_max)
    
    if blocks[i] < cmp:
        ans += cmp - blocks[i]

print(ans)