import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))

def path(x):
    arr = []
    
    tmp = x
    
    for _ in range(cnt[x]+1):
        arr.append(tmp)
        tmp = move[tmp]
    print(' '.join(map(str, arr[::-1])))


def bfs():
    q = deque([])
    q.append(n)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(cnt[x])
            path(x)
            return x

        for i in [x+1, x-1, 2*x]:
            if 0 <= i <= 100000 and cnt[i] == 0:
                q.append(i)
                cnt[i] = cnt[x]+1
                move[i] = x

    
cnt = [0]*100001
move = [0]*100001
bfs()