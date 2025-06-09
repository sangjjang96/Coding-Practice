import sys

n = int(input())

l = list(map(int, sys.stdin.readline().split()))

ans = [-1]*n
s = [0]

for i in range(1, len(l)):
    while s and l[s[-1]] < l[i]:
        ans[s.pop()] = l[i]
    s.append(i)

print(*ans)