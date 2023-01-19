T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))
    arr_sum = sum(arr)
    count = 0

    tmp = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            tmp.append(i+1)
        else:
            tmp.append(i+1+abs(arr[i]))
    print(tmp)
    tmp.sort(reverse=True)
    while 2*N > arr_sum:
        arr_sum += tmp[count]
        count += 1
    print(f'#{test_case} {count}')
