import sys

n, c = list(map(int, sys.stdin.readline().split()))

points = []

for _ in range(n):
    points.append(int(input()))

points.sort()

start = 1
end = points[-1] - points[0]

ans = 0

# [1, 2, 4, 8, 9]
# start = 1, end = 8
# mid = 4
# cur = 1
# 2 1 + 4
# 4 1 + 4
# 8 1 + 4

# cur = 8
# start = 1, end = 3
# mid = 2
# cur = 1
# 2 1 + 2
# 4 1 + 2

# start = 3
# ans = 2

while start <= end:
    mid = (end + start) // 2
    
    cur = points[0]
    count = 1
    
    for i in range(1, len(points)):
        if points[i] >= cur + mid:
            count += 1
            cur = points[i]
    
    if count >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)