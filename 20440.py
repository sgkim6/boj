import sys
from collections import defaultdict

N = int(input())
dic = defaultdict(int)

for i in range(N):
    start, end = map(int, input().split())
    dic[start] += 1
    dic[end] -= 1

count = 0
max_value = 0
top_start = 0
top_end = 0

flag = False

for i in sorted(dic.keys()):
    count += dic[i]
    if count > max_value:  # 현재 모기 수가 역대 기록을 갱신할시
        max_value = count  # 최대값 갱신
        top_start = i
        flag = True
    elif count < max_value and count - dic[i] == max_value and flag:
        top_end = i
        flag = False

print(max_value)
print(top_start, top_end)
