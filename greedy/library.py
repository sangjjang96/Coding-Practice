import sys

n, m = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))

minus = [0]
plus = [0]

for num in nums:
    if num > 0:
        plus.append(num)
    else:
        minus.append(-num)

plus.sort()
minus.sort()

max_val = max(max(plus), max(minus))

ans = 0

while plus:
    ans += plus[-1] * 2
    cnt = 0
    while plus and cnt < m:
        cnt += 1
        plus.pop()

while minus:
    ans += minus[-1] * 2
    cnt = 0
    while minus and cnt < m:
        cnt += 1
        minus.pop()
    
print(ans - max_val)