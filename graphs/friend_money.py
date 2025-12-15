import sys

def find_parents(x):
    if x != parents[x]:
        parents[x] = find_parents(parents[x])
    
    return parents[x]
    
def union_parents(a, b):
    a = find_parents(a)
    b = find_parents(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    

n, m, k = list(map(int, sys.stdin.readline().split()))

relations = []
parents = [0]*(n+1)

money = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(n+1):
    parents[i] = i

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    
    relations.append((a, b))

for a, b in relations:
    if find_parents(a) != find_parents(b):
        union_parents(a, b)
        
print(parents)

total_money = 0

index_per_parents = {}
for i in range(n+1):
    if i == 0:
        continue
    
    if parents[i] in index_per_parents.keys():
        index_per_parents[parents[i]].append(i)
    else:
        index_per_parents[parents[i]] = [i]

for key, val in index_per_parents.items():
    cand = []
    
    for v_ in val:
        cand.append(money[v_])
    
    total_money += min(cand)

if total_money <= k:
    print(total_money)
else:
    print('Oh no')