N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

minimum = 0

A.sort()
B.sort(reverse=True)

for i in range(N):
    minimum += (A[i] * B[i])
    

print(minimum)