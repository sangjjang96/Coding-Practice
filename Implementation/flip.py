import sys

s = sys.stdin.readline()

zeros = []
ones = []

i = 0
while i < len(s)-1:
    idx = i + 1
    
    while s[i] == s[idx]:
        idx += 1
    
    if s[i] == '0':
        zeros.append([i, idx])
    else:
        ones.append([i, idx])
    
    i = idx

print(min(len(zeros), len(ones)))