num = []

def recursion(s, l, r):
    num.append(0)
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = input()

for i in range(int(T)):
    ret = ""
    S = input()
    ret += str(isPalindrome(S))
    ret += " "
    ret += str(len(num))
    print(ret)
    num = []