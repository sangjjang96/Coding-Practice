word = input()

straight = []

for l in word:
    straight.append(l)
    
reverse = straight[::-1]

word_rev = ""

for l in reverse:
    word_rev += l

if word == word_rev:
    print(1)
else:
    print(0)