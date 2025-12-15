import sys

n = int(sys.stdin.readline().rstrip())

ppl = []

for _ in range(n):
    p = int(sys.stdin.readline().rstrip())
    ppl.append(p)

ppl.sort(reverse=True)

ans = 0
for idx, p in enumerate(ppl):
    ans += max(p - idx, 0)

print(ans)