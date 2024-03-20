M, N = input().split()

for i in range(int(M), int(N)+1):
    if i == 2 or i ==3 or i == 5 or i == 7:
        print(i)
    else:
        if i % 2 != 0:
            if i % 3 != 0:
                if i % 5 != 0:
                    if i % 7 != 0:
                            print(i)