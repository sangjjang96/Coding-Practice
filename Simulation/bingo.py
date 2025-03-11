import sys

bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
bingos = [[0]*5 for _ in range(5)]

nums = []

for _ in range(5):
    n = list(map(int, sys.stdin.readline().split()))
    
    for n_ in n:
        nums.append(n_)

print(nums)