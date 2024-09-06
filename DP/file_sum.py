import sys

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    
    pages = [0] + list(map(int, sys.stdin.readline().split()))
    
    cum_sums = [0 for _ in range(K+1)]
    
    for i in range(1, K+1):
        cum_sums[i] = cum_sums[i-1] + pages[i]
    print('cum_sums', cum_sums)
    print()
    
    dp = [[0]*(K+1) for _ in range(K+1)]
    
    for i in range(2, K+1):
        for j in range(1,K+2-i):
            dp[j][j+i-1] =  min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) + (cum_sums[j+i-1] - cum_sums[j-1])
                     
            print('test : ', [dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)])    
            print('i : ', i, 'j: ', j)
            print('cum_sums: ', cum_sums)
            for x in dp:
                print(x)     
            
            
    print(dp[1][K])