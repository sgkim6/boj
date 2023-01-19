def solution(data):
    result = True
    sum = 0

    if '0' not in data:
        print(-1)
        return -1

    data = list(data)

    data.sort(reverse=True)

    data = ''.join(s for s in data)
    data = int(data)

    if data % 3 != 0:
        print(-1)
        return -1
    else:
        print(data)
        return data


N = input()
solution(N)
