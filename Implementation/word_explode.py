import sys

word = sys.stdin.readline().rstrip()

explode = sys.stdin.readline().rstrip()

stack = []
exp_len = len(explode)

for i in range(len(word)):
    stack.append(word[i])
    if ''.join(stack[-exp_len:]) == explode:
        for _ in range(len(explode)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')