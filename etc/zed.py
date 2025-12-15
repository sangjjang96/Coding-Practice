import sys

n, r, c = list(map(int, sys.stdin.readline().split()))

arr = [[0]*(2**n) for _ in range(2**n)]

def zed(arr_in, idx):
    arr_in[0][0] = idx
    arr_in[0][1] = idx+1
    arr_in[1][0] = idx+2
    arr_in[1][1] = idx+3

if n == 1:
    zed(arr, 0)
else:
    
# 00011011 02031213 
# 20213031 22233233

print(arr[r][c])