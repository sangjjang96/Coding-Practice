import sys

n, m = list(map(int, sys.stdin.readline().split()))

prices = []

for _ in range(m):
    price = int(sys.stdin.readline())
    
    prices.append(price)

prices.sort()

max_price = 0
std_price = 0

tmp = 0
for i in range(m):
    p = prices[i]
    
    if p == tmp:
        continue
    
    if max_price < p*(min(n, len(prices)-i)):
        std_price = p
        
    max_price = max(max_price, p*(min(n, len(prices)-i)))
    
    tmp = prices[i]

print(std_price, max_price)