import sys

n = int(input())
k = int(input())

s = 0
e = k

while s <= e:
    m = (s + e) // 2
    cnt = 0
    
    for i in range(1, n+1):
        cnt += min(m//i, n)

    if cnt >= k:
        result = m
        e = m - 1
    else:
        s = m + 1

print(result)
    
    