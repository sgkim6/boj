N = int(input())
L = []

for i in range(N):
    temp = tuple(map(int, input().split()))
    L.append(temp)

L.sort(key=lambda x: (x[1], x[0]))


def result(N, L):
    count = 0
    end = 0
    for i in L:
        if i[0] >= end:
            count += 1
            end = i[1]

    return count


print(result(N, L))
