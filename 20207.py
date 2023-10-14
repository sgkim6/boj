N = int(input())

plans = []  # 시작일, 끝일

answer = 0

calender = [0 for i in range(366)]

slice_idx = 0

for i in range(N):
    S, E = map(int, input().split())
    plans.append((S, E))

for plan in plans:
    start_day = plan[0]
    end_day = plan[1]

    for day in range(start_day, end_day+1):
        calender[day] += 1

max_plan = 0
streak = 0
for day in range(1, 366):
    if calender[day] != 0:
        max_plan = max(max_plan, calender[day])
        streak += 1
    else:
        answer += streak * max_plan
        streak = 0
        max_plan = 0

answer += streak * max_plan
# print(calender)
print(answer)
