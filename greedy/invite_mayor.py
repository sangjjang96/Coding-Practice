import sys

ans = 0

n = int(sys.stdin.readline().rstrip())

trees = list(map(int, sys.stdin.readline().split()))

trees.sort(reverse=True)

for i in range(n):
    ans = max(ans, trees[i] + (i+1) + 1)

print(ans)