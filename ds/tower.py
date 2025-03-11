import sys

n = int(sys.stdin.readline())

towers = sys.stdin.readline().split()

answer = [0]*len(towers)

for i in range(len(towers)):
    for j in range(i, -1, -1):
        if towers[j] > towers[i]:
            answer[i] = j+1
            break
        
print(answer)