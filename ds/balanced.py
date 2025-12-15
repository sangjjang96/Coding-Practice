import sys

while True:
    sentences = sys.stdin.readline()
    
    ans = 'yes'
    
    if sentences[0] == '.':
        break
    
    cur = []
    for s in sentences:
        if s == '(':
            cur.append(0)
        elif s == '[':
            cur.append(1)
        elif s == ')':
            if cur and cur[-1] == 0:
                cur.pop()
            else:
                ans = 'no'
                break
        elif s == ']':
            if cur and cur[-1] == 1:
                cur.pop()
            else:
                ans = 'no'
                break
        else:
            continue
    
    if cur:
        ans = 'no'
    
    print(ans)