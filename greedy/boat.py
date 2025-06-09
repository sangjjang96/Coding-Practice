import sys

n = int(input())

cranes = list(map(int, sys.stdin.readline().split()))

m = int(input())

boxes = list(map(int, sys.stdin.readline().split()))

todos = [[] for _ in range(n)]

if max(boxes) > max(cranes):
    print(-1)
else:
    cnt = 0
    
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)
    
    while boxes:
        for c in cranes:
            if boxes and c < boxes[-1]:
                continue
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break
        cnt += 1
    
    print(cnt)