N = int(input())

A = list(map(int, input().split()))

D = [1]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[j]+1, D[i])

print(max(D))
