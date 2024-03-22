import sys

T = int(input())

for _ in range(T):
    N = int(input())
    
    freshmans = []

    for __ in range(N):
        s1, s2 = list(map(int, sys.stdin.readline().split()))
        freshmans.append((s1, s2))

    freshmans.sort()
    
    std = freshmans[0][1]
    ans = 1
    
    for i in range(1, len(freshmans)):
        if freshmans[i][1] < std:
            ans += 1
            std = freshmans[i][1]
    
    print(ans)