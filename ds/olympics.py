import sys
import heapq

n, k = list(map(int, sys.stdin.readline().split()))

countries = []

ans = 0

for _ in range(n):
    numb, g, s, b = list(map(int, sys.stdin.readline().split()))
    
    heapq.heappush(countries, [-g, -s, -b, numb])
    
    if numb == k:
        g_std, s_std, b_std = g, s, b

while countries:
    g_cur, s_cur, b_cur, n_cur = heapq.heappop(countries)
    
    if -g_cur > g_std:
        ans += 1
    elif -g_cur == g_std:
        if -s_cur > s_std:
            ans += 1
        elif -s_cur == s_std:
            if -b_cur > b_std:
                ans += 1
            elif -b_cur == b_std:
                ans += 1
                break
            else:
                break
        else:
            break
    else:
        ans += 1
        break

print(ans)