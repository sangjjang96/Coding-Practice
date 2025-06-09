import sys
from collections import deque

n, w, l = list(map(int, sys.stdin.readline().split()))

trucks_before = deque(list(map(int, sys.stdin.readline().split())))

trucks_on = deque([])

time = 1
while trucks_before or trucks_on:
    w_sum = 0
    for truck in trucks_on:
        w_sum += truck[0]
    
    if trucks_before:
        if w_sum + trucks_before[0] <= l:
            trucks_on.append([trucks_before.popleft(), w])
    
    for i in range(len(trucks_on)):
        trucks_on[i][1] -= 1
        
    if trucks_on[0][1] <= 0:
        trucks_on.popleft()

    time += 1

print(time)