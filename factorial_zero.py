inp = input()

num = 1
for i in range(1, int(inp)+1):
    num *= i

num_rev = str(num)[::-1]

answer = 0
for i in range(len(num_rev)):
    if num_rev[i] == '0':
        answer += 1
    else:
        break

print(answer)