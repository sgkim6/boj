N = int(input())

flowers = []

answer = 0

for i in range(N):
    start_month, start_day, end_month, end_day = map(int, input().split())
    flowers.append((start_month*50 + start_day, end_month*50 + end_day))

flowers.sort(key=lambda x: (x[0], x[1]))

flowers.append((999999, 99999999))

cur = 151
tmp = 0

for i in range(N):
    start, end = flowers[i]
    if cur < start:
        break
    if cur >= 581:
        break
    #print(start, end)

    # 지금까지 최대값 저장
    if start <= cur:
        tmp = max(tmp, end)

    if flowers[i+1][0] > cur:
        cur = tmp
        answer += 1

if cur >= 581:
    print(answer)
else:
    print(0)
