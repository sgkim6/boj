from collections import deque

N = int(input())

arr = deque(list(map(int, input().split())))
stack = deque()
answer = deque()

while arr:
    tmp = arr.pop()
    if not stack:
        stack.append(tmp)
        answer.append(-1)
        continue

    if stack[-1] > tmp:
        answer.append(stack[-1])
        stack.append(tmp)
    else:
        while stack[-1] <= tmp:
            stack.pop()
            if not stack:
                answer.append(-1)
                break
        if stack:
            answer.append(stack[-1])
        stack.append(tmp)
while answer:
    print(answer.pop(), end=' ')
