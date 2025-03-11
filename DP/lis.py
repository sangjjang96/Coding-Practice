import sys

n = int(input())

dp = [1]*(n)

nums = list(map(int, sys.stdin.readline().split()))

# for i in range(1, n):
#     if nums[i] > max(nums[:i]):
#         idx = nums.index(max(nums[:i]))
#         dp[i] = max(dp[i], dp[idx]+1)

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
        
print(max(dp))