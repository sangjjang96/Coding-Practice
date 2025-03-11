import sys

ans = 0
n = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().split()))

v = int(sys.stdin.readline().rstrip())

nums.sort()

for num in nums:
    if num > v:
        break
    
    if num == v:
        ans += 1
    
print(ans)