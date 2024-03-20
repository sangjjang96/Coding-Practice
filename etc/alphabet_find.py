strings = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

answer = []

strings_l = []

for s in strings:
    strings_l.append(s)

for alpha in alphabet:
    if alpha in strings_l:
        answer.append(strings_l.index(alpha))
    else:
        answer.append(-1)

answer_str = ''
for ans in answer:
    answer_str += str(ans)
    answer_str += ' '
    
print(answer_str)