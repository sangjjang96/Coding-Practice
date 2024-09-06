num = input()

result = 0
for idx, n in enumerate(num):
    if idx == 0:
        result = int(n)
    elif n == '0':
        result += int(n)
    else:
        if num[idx-1] == '0':
            result += int(n)
        else:
            result *= int(n)
    
print(result)