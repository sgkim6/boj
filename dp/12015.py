from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

dp = []

idx = []

for i in arr:
    if not dp:
        dp.append(i)
        continue

    if dp[-1] < i:
        dp.append(i)
    else:
        tmp = bisect_left(dp, i)
        dp[tmp] = i

print(len(dp))
