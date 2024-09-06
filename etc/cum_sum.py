import sys

N, S = list(map(int, sys.stdin.readline().split()))

nums = list(map(int, sys.stdin.readline().split()))


inf = 100000
length = inf

left = 0
right = 0
sum_tmp = nums[0]

while left <= right:
    if sum_tmp >= S:
        length = min(length, right-left + 1)
        sum_tmp -= nums[left]
        left += 1
    else:
        right += 1
        if right < N:
            sum_tmp += nums[right]
        else:
            break

if length == 100000:
    print(0)
else:
    print(length)