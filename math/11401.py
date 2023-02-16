import math
N,K = map(int,input().split())

factorial = [1,1]
for i in range(2,N+1):
    factorial.append(factorial[-1]*i)

print((factorial[N]//factorial[K])//factorial[N-K])

