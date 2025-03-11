import sys

n = int(input())

budgets = list(map(int, sys.stdin.readline().split()))

limit = int(input())

start, end = 0, max(budgets)

std_sum = []

while start <= end:
    mid = (start + end) // 2
    summ = 0
    
    for budget in budgets:
        if budget >= mid:
            summ += mid
        else:
            summ += budget
    
    if summ < limit and [mid, summ] not in std_sum:
        std_sum.append([mid, summ])
    
    if summ <= limit:
        start = mid+1
    else:
        end = mid-1

print(end)