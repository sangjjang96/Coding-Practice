import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    N, M = list(map(int, sys.stdin.readline().split()))

    script = list(map(int, sys.stdin.readline().split()))

    tmp = []
    for idx, s in enumerate(script):
        tmp.append([s, idx])
        
    q = deque(script)
    q_ = deque([i for i in range(N)])

    result = []

    while q:
        maximum = max(q)

        x = q.popleft()
        idx = q_.popleft()
        
        if x == maximum:
            result.append(idx)
        else:
            q.append(x)
            q_.append(idx)

    print(result.index(M)+1)