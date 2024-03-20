n = int(input())

scores = [0]*301
dp = [0]*301

for i in range(1, n+1):
    score = int(input())
    scores[i] = score
    
dp[1] = scores[1]
dp[2] = scores[1] + scores[2]
dp[3] = max(scores[1]+scores[3], scores[2]+scores[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2] + scores[i])

print(dp[n])