import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

operators = list(map(int, sys.stdin.readline().split()))

mini = int(1e9)
maxi = int(-1e9)

def dfs(n, num):
    global mini, maxi
    
    if n == N-1:
        maxi = max(num, maxi)
        mini = min(num, mini)
        return
    
    if operators[0] != 0:
        operators[0] -= 1
        dfs(n+1, num + A[n+1])
        operators[0] += 1
    
    if operators[1] != 0:
        operators[1] -= 1
        dfs(n+1, num - A[n+1])
        operators[1] += 1
    
    if operators[2] != 0:
        operators[2] -= 1
        dfs(n+1, num * A[n+1])
        operators[2] += 1
        
    if operators[3] != 0:
        operators[3] -= 1
        dfs(n+1, int(num / A[n+1]))
        operators[3] += 1
        
dfs(0, A[0])
print(maxi)
print(mini)