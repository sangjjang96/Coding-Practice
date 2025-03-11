import sys

T = int(input())

for _ in range(T):
    n = int(input())
    ans = 0
    
    prices = list(map(int, sys.stdin.readline().split()))
    
    max_p = 0
    
    for i in range(len(prices)-1, -1, -1):
        if prices[i] > max_p:
            max_p = prices[i]
        else:
            ans += (max_p - prices[i])
    
    print(ans)