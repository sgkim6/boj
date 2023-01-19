N = int(input())


def result(N):
    count = 0

    while(N % 5 != 0):
        N -= 3
        count += 1
        if N == 1 or N == 2:
            print(-1)
            return

    count += N/5

    print(int(count))
    return


result(N)
