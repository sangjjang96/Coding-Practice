import math

n = int(input())

arr = [True]*(n+1)

for i in range(2, int(math.sqrt(n+1))+1):
    if arr[i]:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1

for i in range(len(arr)):
    if arr[i] and i >= 2:
        print(i)
    