import sys
import heapq

n = int(sys.stdin.readline().rstrip())

courses = []

for _ in range(n):
    num_course, start, end = list(map(int, sys.stdin.readline().split()))
    
    courses.append((start, end, num_course))

courses.sort(key=lambda x: (x[0]))

classes = [courses[0][1]]

ans = 0
for i in range(1, n):
    while classes and courses[i][0] >= classes[0]:
        heapq.heappop(classes)
    heapq.heappush(classes, courses[i][1])
    
    ans = max(ans, len(classes))

print(ans)