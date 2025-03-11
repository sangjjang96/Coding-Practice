import sys

n = int(sys.stdin.readline())


weights = [0] + list(map(int, sys.stdin.readline().split()))
cum = [0]

weights.sort()

for i in range(len(weights)):
    cum.append(cum[i] + weights[i])

cum = cum[1:]

for i in range(len(weights)):
    if weights[i] > cum[i-1]+1:
        print(cum[i-1]+1)
        break
    
    if i == len(weights)-1:
        print(sum(weights)+1)