n = int(input())
A = list(map(int, input().split()))
result = 0

for i in range(1, n-1):
    lc = 0
    rc = 0
    for j in range(0, i):
        if A[i] > A[j]:
            lc += 1
    for j in range(i+1, n):
        if A[i] > A[j]:
            rc += 1
    result += lc*rc

print(result)
