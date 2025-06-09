import sys

n = int(input())

trees = list(map(int, sys.stdin.readline().split()))

to_del = int(input())

def dfs(del_node):
    trees[del_node] = -2
    for i in range(n):
        if del_node == trees[i]:
            dfs(i)

dfs(to_del)
cnt = 0

for i in range(n):
    if trees[i] != -2 and i not in trees:
        cnt += 1

print(cnt)