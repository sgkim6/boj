import heapq
from collections import deque

arr = list(map(int, input().split()))

answer = 0

left_stack = []
right_stack = []
length = len(arr)

for i in range(len(arr)):
    if i == 0:
        left_stack.append(arr[i])
    else:
        if left_stack[-1] > arr[i]:
            left_stack.append(arr[i])
        else:
            left_stack.append(left_stack[-1])

    j = length - 1 - i
    if j == length-1:
        right_stack.append(arr[j])
    else:
        if right_stack[-1] > arr[j]:
            right_stack.append(arr[j])
        else:
            right_stack.append(right_stack[-1])

for i in range(len(arr)):
    if i == 0 or i == length-1:
        answer += 1
    else:
        tmp = 0
        if arr[i] > left_stack[i-1]:
            tmp += 1
        if arr[i] > right_stack[length-2-i]:
            tmp += 1
        if tmp < 2:
            answer += 1

print(answer)
