import math
for test_case in range(1,int(input())+1):
    N, M = map(int,input().split())
    print(math.comb(M,N))