N = input()
N_arr = input().split()
M = input()
M_arr = input().split()

A = {}

for n in N_arr:
    A[n] = 0

for m in M_arr:
    if m in A.keys():
        print(1)
    else:
        print(0)