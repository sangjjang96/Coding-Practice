import sys

ans = 0
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    not_group = False
    alphabets = {}
    
    word = str(sys.stdin.readline().rstrip())
    
    before = ' '
    
    for w in word:
        if before == ' ':
            alphabets[w] = 0
            alphabets[w] += 1
            before = w
                
        if w == before:
            continue
        
        if w != before and w not in alphabets.keys():
            alphabets[w] = 0
            alphabets[w] += 1
            before = w
        else:
            not_group = True
            break
    
    if not not_group:
        ans += 1

print(ans)