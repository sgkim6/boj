N = int(input())

arr_x = []
arr_y = []

for _ in range(N):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

arr_x.append(arr_x[0])
arr_y.append(arr_y[0])

sum_1 = 0
sum_2 = 0

for i in range(N):
    sum_1 += arr_x[i] * arr_y[i+1]
    sum_2 += arr_x[i+1] * arr_y[i]

print(round(abs((sum_1 - sum_2)/2), 1))
