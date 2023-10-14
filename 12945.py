N = int(input())

arr = []

clear = 0

for i in range(N):
    arr.append(int(input()))

arr.sort()

left_arr = arr[:N//2]
right_arr = arr[N//2:]

while left_arr:
    box = left_arr.pop()
    if right_arr[-1] >= box*2:
        right_arr.pop()
        clear += 1

print(N-clear)
