import sys

n, c = list(map(int, sys.stdin.readline().split()))

points = []

for _ in range(n):
    points.append(int(input()))

points.sort()

print(points)