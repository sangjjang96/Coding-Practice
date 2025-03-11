import sys

n = int(input())

limits = list(map(int, sys.stdin.readline().split()))
cranes = []
for _ in range(n):
    cranes.append([])

limits.sort()

m = int(input())

boxes = list(map(int, sys.stdin.readline().split()))
boxes.sort()

idx = 0
for box in boxes:
    for i in range(len(cranes)):
        if box <= limits[i]:
            cranes[i].append(box)
        
print(cranes)