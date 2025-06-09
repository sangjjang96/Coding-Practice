import sys
import heapq

n = int(input())

cups = []
q = []

for _ in range(n):
    deadline, num = list(map(int, sys.stdin.readline().split()))

    cups.append((deadline, num))

cups.sort(key=lambda x: (x[0], -x[1]))

t, ans = 1, 0

for d, n in cups:
    if t <= d:
        ans += n
        heapq.heappush(q, (n, t))
        t += 1
    else:
        if q:
            min_tmp = heapq.heappop(q)
            if min_tmp[0] < n:
                ans += (n-min_tmp[0])
                heapq.heappush(q, (n, min_tmp[1]))
            else:
                heapq.heappush(q, min_tmp)

print(ans)