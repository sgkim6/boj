N = int(input())


answer = 0
answer_set = []
branches = []

arr = [0]

tuples = []
for _ in range(N):
    arr.append(int(input()))

arr_set = set(arr)

for i in range(1, N+1):
    tuples.append((arr[i], i))
tuples.sort()

tmp_set = set()
tmp_arr = [0]

for i in range(0, N):

    if i == 0:
        if tuples[i][1] in arr_set:
            tmp_arr.append(tuples[i][1])
    else:
        if tuples[i][0] == tuples[i-1][0]:  # 방금 전꺼랑 같으면
            if tuples[i][1] in arr_set:
                tmp_arr.append(tuples[i][1])
        else:
            if len(tmp_arr) > 1:
                branches.append(tmp_arr[:])
            tmp_arr = [0]
            if tuples[i][1] in arr_set:
                tmp_arr.append(tuples[i][1])
if len(tmp_arr) > 1:
    branches.append(tmp_arr)

print(branches)

for branch in branches:
    for i in branch:
