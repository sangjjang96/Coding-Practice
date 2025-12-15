import sys

ans = 0

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

if m > 0:
    broken = list(map(int, sys.stdin.readline().split()))
else:
    broken = []

ans = abs(100 - n)

for num in range(1000001):
    n_str = str(num)
    
    for j in range(len(n_str)):
        if int(n_str[j]) in broken:
            break
        
        elif j == len(n_str) -1:
            ans = min(ans, abs(num - n) + len(n_str))
    
print(ans)