from collections import defaultdict, deque

N = int(input())

time = [0 for i in range(N+1)]

for i in range(1, N+1):
    tmp = input().split()

    if int(tmp[1]) == 0:  # 선행 작업이 없을 경우 바로 ㄱㄱ
        time[i] = int(tmp[0])
        continue

    s = 0
    for target in tmp[2:]:  # 선행 작업이 있을 경우 -> 선행 작업들 중 가장 오래 걸리는 녀석의 시간 + 지금 작업 시간
        s = max(time[int(target)], s)
    time[i] = int(tmp[0]) + s

print(max(time))
