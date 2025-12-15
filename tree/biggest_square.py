import sys
from collections import deque

while True:   
    histograms = list(map(int, sys.stdin.readline().split()))
    
    n = histograms[0]
    
    if n == 0:
        break
    
    s = []                                                      # (idx, height)
    
    ans = 0
    
    for i in range(1, n+1):
        if len(s) == 0:
            s.append((i, histograms[i]))
        else:
            if s[-1][1] <= histograms[i]:                       # 커지는 경우
                s.append((i, histograms[i]))
            else:                                               # 작아지는 경우
                while len(s) > 0 and s[-1][1] > histograms[i]:
                    remove = s.pop()
                    if len(s) == 0:
                        w = i-1
                    else:
                        w = i-s[-1][0]-1
                    ans = max(ans, remove[1]*w)
                s.append((i, histograms[i]))
    
    while s:                                                    # 증가하기만 하는 경우
        remove = s.pop()
        
        if len(s) == 0:
            w = n
        else:
            w = n-s[-1][0]
        ans = max(ans, remove[1]*w)
    
    print(ans)
                
                
                
                