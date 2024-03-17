n = input()

for i_ in range(int(n)):
    summ = 0
    ans = 0
    quiz = input().split()

    for i in range(len(quiz[0])):
        if i == 0:
            if quiz[0][i] == 'O':
                summ += 1
            else:
                summ = 0
            
            ans += summ
        else:
            if quiz[0][i] == 'O':
                summ += 1
            else:
                summ = 0
            
            ans += summ

    print(ans)   