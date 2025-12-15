import sys

n = int(sys.stdin.readline())

inp_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


for k in range(n):
    for a in range(n):
        for b in range(n):
            if inp_list[a][k] and inp_list[k][b]:
                inp_list[a][b] = 1

for inp in inp_list:
    print(*inp)