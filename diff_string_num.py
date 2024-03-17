S = input()
S_list = []

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        S_list.append(S[i:j])

S_list = list(set(S_list))
print(len(S_list))