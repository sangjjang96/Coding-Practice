N = input()
nums_have = input().split()

M = input()
nums_define = input().split()

nums_have_dic = {n: 1 for n in nums_have}

result = ""

for i in range(int(M)):
    if nums_define[i] in nums_have_dic:
        result += "1"
    else:
        result += "0"
    result += " "

print(result)