word = input()

num = 0
w = {}
multi = False

for l in word:
    if l.lower() not in w:
        w[l.lower()] = 0
    w[l.lower()] += 1
    
for k, v in w.items():
    if int(v) > num:
        multi = False
        result = k
        num = int(v)
    elif int(v) == num:
        multi = True
        
if multi == False:
    print(result.upper())
else:
    print("?")