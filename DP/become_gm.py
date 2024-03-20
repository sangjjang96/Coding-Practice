T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    
    dp = [0]*((k+1)*n)
    
    for j in range(0, n):
        dp[j] = j+1
    
    for j in range(0, (k+1)*n, n):
        dp[j] = 1
    
    for j in range(n+1, (k+1)*n):
        if j % n == 0:
            continue
        dp[j] = dp[j-1] + dp[j-n]
    
    print(dp[(k+1)*n - 1])