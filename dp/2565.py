from bisect import bisect_left
import sys
input = sys.stdin.readline

T = int(input())
L = []
for i in range(T):
    a, b = map(int, input().split())
    L.append([a, b])
L.sort(key=lambda x: x[0])

dp = []

check = []
for i, j in L:
    if not dp:
        dp.append(j)
    if dp[-1] < j:
        dp.append(j)
        check.append((len(dp)-1, j))
    else:
        index = bisect_left(dp, j)
        dp[index] = j
        check.append((index, j))


answer = []

last_index = len(dp)-1

for i in range(len(check)-1, -1, -1):
    if check[i][0] == last_index:
        answer.append(check[i][1])
        last_index -= 1
print(dp)

print(T-len(dp))
A_line = []

for i in range(-1, -T-1, -1):
    for j in range(len(answer)):
        if L[i][1] == answer[j]:
            A_line.append(L[i][0])


A_line.sort()
count = 0

for i in range(T):
    P = 0
    for j in range(len(A_line)):
        if L[i][0] == A_line[j]:
            P = 1
    if P == 0:
        print(L[i][0])
