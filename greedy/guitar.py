import sys

n, m = list(map(int, sys.stdin.readline().split()))

prices_six = []
prices_one = []

for _ in range(m):
    price_six, price_one = list(map(int, sys.stdin.readline().split()))
    prices_six.append(price_six)
    prices_one.append(price_one)

min_one = min(prices_one)
min_six = min(prices_six)

ans = 0
while n > 0:
    if n >= 6:
        min_single = min_one*6
        n -= 6
    else:
        min_single = min_one*n
        n -= n
    if min_single < min_six:
        ans += min_one
    else:
        ans += min_six

print(ans)