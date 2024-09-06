from itertools import combinations

L, C = list(map(int, input().split()))

letters = list(map(str, input().split()))
letters.sort()

comb = combinations(letters, L)

answer = []
for co in comb:
    l = ''
    for c in co:
        l += c
    
    answer.append(l)

alphabet = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for a in answer:
    if 'a' in a or 'e' in a or 'i' in a or 'o' in a or 'u' in a:
        num = 0
        for alpha in alphabet:
            if alpha in a:
                num += 1
                if num >= 2:
                    print(a)
                    break