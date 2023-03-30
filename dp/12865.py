N, K = map(int,input().split())

arr = [(0,0)]

for _ in range(N):
    weight, value = map(int,input().split())
    arr.append((weight,value))

bag = [[0 for i in range(K+1)] for j in range(N+1)]

for row in range(1,N+1):
    for col in range(1,K+1):
        weight = arr[row][0]
        value = arr[row][1]

        if col < weight:
            bag[row][col] = bag[row-1][col]
        else:
            bag[row][col] = max(bag[row-1][col-weight] + value, bag[row-1][col])

print(bag[N][K])