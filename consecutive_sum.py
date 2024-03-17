n = int(input())

l = list(map(int, input().split()))

for i in range(1, n):
    l[i] = max(l[i], l[i]+l[i-1])

print(max(l))