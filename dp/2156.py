n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

D = [0]*(n+1)

D[0] = A[0]
if n >= 2:
    D[1] = A[0]+A[1]
if n >= 3:
    D[2] = max(A[2]+A[1], A[2]+A[0], A[1]+A[0])
if n >= 3:
    for i in range(3, n):
        D[i] = max(D[i-1], A[i-1]+A[i]+D[i-3], A[i]+D[i-2])

print(D[n-1])
