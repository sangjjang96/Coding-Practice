T = input()

brackets = []

for i in range(int(T)):
    bracket = input()
    brackets.append(bracket)
    
for bracket in brackets:
    done = False
    stack = []
    for b in bracket:
        if b == "(":
            stack.append(1)
        elif b == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                done = True
                break
    
    if done != True:  
        if not stack:
            print("YES")
        else:
            print("NO")