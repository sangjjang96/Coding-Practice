N, M = input().split()

nums = input().split()

for i in range(int(N)):
    nums[i] = int(nums[i])
    
result = 0

for i in range(int(N)-2):
    for j in range(i+1, int(N)-1):
        for k in range(j+1, int(N)):
            n = nums[i] + nums[j] + nums[k]
            if n > result and n <= int(M):
                r_i = i
                r_j = j
                r_k = k
                result = n
                   
print(result)