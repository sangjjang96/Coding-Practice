N = int(input())

from collections import deque
deque = deque([])

import sys

for _ in range(N):
    command = list(map(str, sys.stdin.readline().split()))
    
    if len(command) > 1:
        if command[0] == 'push_front':
            deque.appendleft(int(command[1]))
        elif command[0] == 'push_back':
            deque.append(int(command[1]))
    else:
        if command[0] == 'front':
            if deque:
                print(deque[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if deque:
                print(deque[-1])
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(deque))
        elif command[0] == 'empty':
            if deque:
                print(0)
            else:
                print(1)
        elif command[0] == 'pop_front':
            if deque:
                deque.popleft()
            else:
                print(-1)
        elif command[0] == 'pop_back':
            if deque:
                deque.pop()
            else:
                print(-1)