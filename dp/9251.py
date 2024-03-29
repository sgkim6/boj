str1 = input()
str2 = input()

col = len(str1)
row = len(str2)

dp = [[0 for i in range(col+1)] for j in range(row+1)]

for i in range(1,row+1):
    for j in range(1,col+1):
        if (str2[i-1] == str1[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[row][col])