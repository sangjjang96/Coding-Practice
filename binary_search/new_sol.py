import sys

n = int(sys.stdin.readline())

sol = list(map(int, sys.stdin.readline().split()))

sol.sort()

std = int(1e12)

for i in range(n-2):
    start = i+1
    end = n-1

    while start < end:        
        summ = sol[start] + sol[i] + sol[end]
        
        if abs(summ) < std:
            std = abs(summ)
            ans = [sol[start], sol[i], sol[end]]
        
        if summ < 0:
            start += 1
        elif summ > 0:
            end -= 1
        else:
            break

ans.sort()

print(*ans)