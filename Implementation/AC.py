from collections import deque
import sys

T = int(input())

for _ in range(T):
    p = sys.stdin.readline()

    n = int(sys.stdin.readline())

    x = sys.stdin.readline().rstrip()
    
    l = deque([])
    for inp in x:
        if inp == '[' or inp == ']' or inp == ',':
            continue
        
        l.append(int(inp))
    
    broken = False
    for command in p:
        if len(l) == 0:
            broken = True
            break
        if command == 'R':
            l.reverse()
        elif command == 'D':
            l.popleft()
    
    if broken:
        print('error')
    else:
        print(list(l))