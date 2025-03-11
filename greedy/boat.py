import sys

n = int(input())

cranes = list(map(int, sys.stdin.readline().split()))

m = int(input())

boxes = list(map(int, sys.stdin.readline().split()))

if max(boxes) > max(cranes):
    print(-1)
else:
    cranes.sort()
    boxes.sort()
    
    box_avail = []
    
    idx = 0
    for i in range(len(boxes)):
        if boxes[i] > cranes[idx]:
            box_avail.append(i)
            idx += 1
            
    if len(box_avail) != len(cranes):
        for _ in range(len(cranes) - len(box_avail)):
            box_avail.append(len(boxes))
    
    print(cranes)
    print(box_avail)
    print(boxes)