import sys

S = list(map(str, sys.stdin.readline().split()))

answer = ''
for s in S:
    
    answer += s[::-1]
    answer += ' '

print(answer)