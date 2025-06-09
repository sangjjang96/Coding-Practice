import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

l = []
seg_tree = [0]*(n*4)
    
def init(s, e, idx):
    if s == e:
        seg_tree[idx] = l[s-1]
        return seg_tree[idx]

    mid = (s + e) // 2
    seg_tree[idx] = init(s, mid, idx*2) + init(mid + 1, e, idx*2 + 1)
    return seg_tree[idx]

def find(s, e, idx, left, right):
    if s > right or e < left:
        return 0
    
    if s >= left and e <= right:
        return seg_tree[idx]
    
    mid = (s + e) // 2
    sub_sum = find(s, mid, idx*2, left, right) + find(mid+1, e, idx*2 + 1, left, right)
    return sub_sum

def update(s, e, idx, update_idx, update_d):
    if s > update_idx or e < update_idx:
        return
    
    seg_tree[idx] += update_d
    
    if s == e:
        return
    
    mid = (s + e) // 2
    update(s, mid, idx*2, update_idx, update_d)
    update(mid+1, e, idx*2 + 1, update_idx, update_d)
    
for _ in range(n):
    l.append(int(input()))

init(1, n, 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        tmp = c - l[b-1]
        l[b-1] = c
        update(1, n, 1, b, tmp)
        
    elif a == 2:
        print(find(1, n, 1, b, c))