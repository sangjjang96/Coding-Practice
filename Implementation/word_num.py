t = int(input())

for i in range(t):
    str1 = input()
    str2 = input()
    
    dic_1 = {}
    
    for s in str1:
        dic_1[s] = 0
    
    for s in str2:
        if s in dic_1.keys():
            dic_1[s] += 1
    
    max_num = 0
    
    for k, v in dic_1.items():
        max_num = max(max_num, v)
        
    
    print(f'#{i+1} {max_num}')