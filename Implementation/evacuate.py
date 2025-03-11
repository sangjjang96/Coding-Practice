import sys
from itertools import *

n, k = list(map(int, sys.stdin.readline().split()))

houses = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def distance(house, evac):
    return abs(house[0] - evac[0]) + abs(house[1] - evac[1])

inf = int(1e9)
std = inf

for cand in combinations(houses, k):
    maxi = 0
    for house in houses:
        max_std = inf
        for c in cand:
            max_std = min(distance(house, c), max_std)
        std = max(max_std, std)

    std = min(max_std, std)

print(std)