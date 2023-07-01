import math

N = int(input())

max_answer = 0
min_answer = int(1e9)


def divide(N, count):
    global max_answer, min_answer
    if 0 < N < 10:
        count = count + (N % 2)
        if max_answer < count:
            max_answer = count
        if min_answer > count:
            min_answer = count
        return

    if 10 <= N < 100:
        count += (N//10) % 2 + (N % 2)
        divide((N//10 + N % 10), count)

    if 100 <= N:
        for i in range(9):
            count += N//(10**i) % 2

        digit = int(math.log10(N)) + 1
        for i in range(1, digit):
            for j in range(i+1, digit):  # 숫자 사이 기준 오른쪽부터 i, j 자르기
                num1 = N//(10**j)
                num2 = N % (10**j) // (10**i)
                num3 = N % (10**i)
                divide((num1+num2+num3), count)


divide(N, 0)
print(min_answer, max_answer)
