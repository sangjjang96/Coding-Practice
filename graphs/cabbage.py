T = int(input())

M, N, K = list(map(int, input().split()))

ground = [[0] * N for _ in range(M)]

for _ in range(K):
    x, y = list(map(int, input().split()))
    ground[x][y] = 1

for g in ground:
    print(g)