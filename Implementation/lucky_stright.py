num = input()

half = len(num) // 2
left = num[:half]
right = num[half:]

l = 0
r = 0

for le in left:
    l += int(le)

for ri in right:
    r += int(ri)
    
if l == r:
    print('LUCKY')
else:
    print('READY')