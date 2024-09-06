S = input()
strings = []
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


for s in S:
    strings.append(s)
    
strings.sort()

result = ''
num = 0

for s in strings:
    if s in number:
        num += int(s)
    else:
        result += s

result += str(num)
print(result)