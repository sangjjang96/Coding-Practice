import sys

n = int(sys.stdin.readline().rstrip())

ropes = []

for _ in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))
ropes.sort(reverse=True)

result = ropes[0]

for i in range(1, n):
    result = max(result, ropes[i]*(i+1))
    
print(result)