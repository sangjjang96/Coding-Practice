import sys

ans = 0

n = int(sys.stdin.readline().rstrip())

price_info = []

lengths = list(map(int, sys.stdin.readline().split()))

prices = list(map(int, sys.stdin.readline().split()))

minimum = int(1e9)
for i in range(len(prices)):
    minimum = min(minimum, prices[i])
    prices[i] = minimum

for i in range(len(lengths)):
    ans += (lengths[i] * prices[i])
    
print(ans)