import sys

n, c = list(map(int, sys.stdin.readline().split()))

poses = []

for _ in range(n):
    poses.append(int(sys.stdin.readline()))
    
poses.sort()

start = 1
end = poses[-1] - poses[0]

while start <= end:
    mid = (start + end) // 2
    
    cur = poses[0]
    count = 1
    
    for i in range(1, len(poses)):
        if poses[i] >= cur + mid:
            count += 1
            cur = poses[i]
    
    if count >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
        
print(ans)