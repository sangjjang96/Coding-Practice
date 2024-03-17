N = input()

result = 0

for i in range(int(N)-1):
    nn = 0
    for n in str(i):
        nn += int(n)
    
    if i + nn == int(N):
        result = i
        break
        
print(result)