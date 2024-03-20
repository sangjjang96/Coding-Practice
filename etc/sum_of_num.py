S = int(input())

if S == 1:
    print(1)
else:
    for i in range(2, S):
        if (i+1) * ((i+1)//2) == S:
            print(i)
            break