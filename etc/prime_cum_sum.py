import sys

N = int(sys.stdin.readline())

if N == 1:
    print(0)
else:
    inf = int(1e10)
    left = 0
    right = 0

    primes = [False, False] + [True]*(N-1)
    prime_num = []

    for i in range(2, N+1):
        if primes[i]:
            prime_num.append(i)
            for j in range(2*i, N+1, i):
                primes[j] = False

    answer = 0
    sum_tmp = prime_num[0]

    while right <= len(prime_num):
        temp_sum = sum(prime_num[left:right])
        if temp_sum == N:
            answer += 1
            right += 1
        elif temp_sum < N:
            right += 1
        else:
            left += 1

    print(answer)
        