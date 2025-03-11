import sys
import heapq

n = int(sys.stdin.readline())

q = list(map(int, sys.stdin.readline().split()))

l = [0]*21
l[0] = 1

for i in range(1, n+1):
    l[i] = l[i-1] * i

visited = [False]*21

s = [0]*21

if q[0] == 1:
    k = q[1]
    for i in range(1, n+1):
        cnt = 1 
        for j in range(1, n+1):
            if visited[j]: 
                continue
            if k <= cnt * l[n-i]: 
                k -= (cnt-1) * l[n-i]

                s[i] = j
                visited[j] = True
                break
            cnt += 1

    for i in range(1, n+1):
        print(s[i], end=" ")
else:
    k = 1 
    for i in range(1, n+1):
        cnt = 0

        for j in range(1, q[i]):
            if not visited[j]:
                cnt += 1

        k += cnt * l[n-i]
        visited[q[i]] = True

    print(k)