import sys
import heapq

n = int(sys.stdin.readline())

poses = list(map(int, sys.stdin.readline().split()))

arr = sorted(set(poses))

dic = {arr[i]:i for i in range(len(arr))}

ans = []
for p in poses:
    ans.append(dic[p])

print(*ans)