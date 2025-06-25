n = int(input())
dp = [[0,0,0] for _ in range(n+1)]

dp[1][1] = 1
dp[1][2] = 0
if n >= 2:
    dp[2][1] = 1
    dp[2][2] = 2
for i in range(3, n+1):
    dp[i][1] = sum(dp[i-1])
    dp[i][2] = 2 * sum(dp[i-2])
answer = sum(dp[n]) % 10007
print(answer)