T = int(input())
P = [1,1,1,2,2,3,4,5,7,9,]

for i in range(90):
    P.append(P[-1]+P[-5])

for _ in range(T):
    N = int(input())
    print(P[N-1])

