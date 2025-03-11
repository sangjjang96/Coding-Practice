import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

q = deque([])

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()

    if ' ' in cmd:
        cmd = cmd.split(' ')
        
        if cmd[0] == 'push':
            q.append(int(cmd[1]))

    else:
        cmd = str(cmd)
        
        if cmd == 'pop':
            if q:
                print(q.pop())
            else:
                print(-1)
        elif cmd == 'size':
            print(len(q))
        elif cmd == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif cmd == 'top':
            if q:
                print(q[-1])
            else:
                print(-1)