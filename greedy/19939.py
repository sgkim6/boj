N,K = map(int,input().split())

s = K*(K+1)//2 

if K*(K+1)//2 > N:
    print(-1)
elif (N-s)%K == 0:
    print(K-1)
else:
    print(K)