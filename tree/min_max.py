import sys

n, m = list(map(int, sys.stdin.readline().split()))

l = []

seg_tree_max = [0]*(n*4)
seg_tree_min = [int(1e9)]*(n*4)

for _ in range(n):
    l.append(int(sys.stdin.readline()))
    
def init_max(s, e, idx):
    if s == e:
        seg_tree_max[idx] = l[s-1]
        return seg_tree_max[idx]

    mid = (s + e) // 2
    seg_tree_max[idx] = max(init_max(s, mid, idx*2), init_max(mid + 1, e, idx*2 + 1))
    return seg_tree_max[idx]

def init_min(s, e, idx):
    if s == e:
        seg_tree_min[idx] = l[s-1]
        return seg_tree_min[idx]

    mid = (s + e) // 2
    seg_tree_min[idx] = min(init_min(s, mid, idx*2), init_min(mid + 1, e, idx*2 + 1))
    return seg_tree_min[idx]

    
def find_max(s, e, idx, left, right):
    if s > right or e < left:
        return 0
    
    if s >= left and e <= right:
        return seg_tree_max[idx]
    
    mid = (s + e) // 2
    
    ld = find_max(s, mid, idx*2, left, right)
    rd = find_max(mid+1, e, idx*2 + 1, left, right)
    
    return max(ld, rd)

def find_min(s, e, idx, left, right):
    if s > right or e < left:
        return int(1e9)
    
    if s >= left and e <= right:
        return seg_tree_min[idx]
    
    mid = (s + e) // 2

    ld = find_min(s, mid, idx*2, left, right)
    rd = find_min(mid+1, e, idx*2 + 1, left, right)
    
    return min(ld, rd)

init_min(1, n, 1)
init_max(1, n, 1)

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    result_min = find_min(1, n, 1, a, b)
    result_max = find_max(1, n, 1, a, b)

    print(result_min, result_max)
    