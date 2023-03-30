T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = []
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
    dp = [[0 for i in range(n)] for j in range(2)]
    if(n == 1):
        print(max(arr[0][-1], arr[1][-1]))
    else:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]

        print(max(dp[0][-1], dp[1][-1]))
