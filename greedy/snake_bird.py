import sys

answer = 0

n, l = list(map(int, sys.stdin.readline().split()))

foods = list(map(int, sys.stdin.readline().split()))

foods.sort()

for food in foods:
    if l >= food:
        answer = food
        l += 1

print(l)