import sys

n = int(sys.stdin.readline())

solutions = list(map(int, sys.stdin.readline().split()))

solutions.sort()

left = 0
right = len(solutions)-1

ans = []
min_sum = int(1e11)
left_tmp = 0
right_tmp = 0

while left < right:
    summ = solutions[left] + solutions[right]

    if summ > 0:
        if summ < min_sum:
            min_sum = min(summ, min_sum)
            left_tmp = left
            right_tmp = right
        right -= 1
    elif summ == 0:
        ans.append(solutions[left])
        ans.append(solutions[right])
        break
    else:
        if abs(summ) < min_sum:
            min_sum = min(abs(summ), min_sum)
            left_tmp = left
            right_tmp = right
        left += 1

if ans:
    print(*ans)
else:
    print(solutions[left_tmp], solutions[right_tmp])
     