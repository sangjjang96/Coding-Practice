N, M = input().split()

S = []
ToVerify = []

for i in range(int(N)):
    s = input()
    S.append(s)
    
for i in range(int(M)):
    tv = input()
    ToVerify.append(tv)
    
result = 0

for tv in ToVerify:
    if tv in S:
        result += 1
        
print(result)