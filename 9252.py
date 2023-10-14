A = input()
B = input()

A = " "+A
B = " "+B

dp = [["" for i in range(len(B))] for j in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + A[i]
        else:
            if len(dp[i][j-1]) >= len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

print(len(dp[-1][-1]))
if len(dp[-1][-1]) != 0:
    print(dp[-1][-1])
