import sys
from collections import deque

answer = 0

S = str(sys.stdin.readline().rstrip())
T = str(sys.stdin.readline().rstrip())

if S == T:
    answer = 1
    
q = deque([])
q.append(T)

while q:
    w = q.popleft()
    
    if w == S:
        answer = 1
    
    if w[-1] == 'A':
        w = w[:(len(w)-1)]
        
    elif w[-1] == 'B':
        w = w[:(len(w)-1)]
        w = w[::-1]

    if len(w) >= len(S):
        q.append(w)

print(answer)