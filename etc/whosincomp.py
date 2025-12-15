import sys

n = int(input())

dic = {}

for _ in range(n):
    name, status = list(map(str, sys.stdin.readline().split()))
    
    if status == 'enter':
        dic[name] = 1
    else:
        dic[name] = 0

ans = []
for k, v in dic.items():
    if v == 1:
        ans.append(k)

ans.sort(reverse=True)
for a in ans:
    print(a)