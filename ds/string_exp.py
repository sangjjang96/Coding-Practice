import sys

given = input()
exp = input()

s = []

for i in range(len(given)):
    s.append(given[i])
    if ''.join(s[-len(exp):]) == exp:
        for _ in range(len(exp)):
            s.pop()

if s:
    print(''.join(s))
else:
    print('FURLA')
    