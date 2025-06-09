import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))

conveyer = []

boxes = list(map(int, sys.stdin.readline().split()))

conveyer.append(deque(boxes[:n]))
conveyer.append(deque(boxes[n:]))

steps = 0



print(conveyer)