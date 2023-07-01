from collections import deque

S = list(input())

stack = deque()

for char in S:
    stack.append(char)

    if len(stack) >= 4:
        if stack[-4] == 'P' and stack[-3] == 'P' and stack[-2] == 'A' and stack[-1] == 'P':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('P')

if list(stack) == ['P']:
    print('PPAP')
else:
    print('NP')
