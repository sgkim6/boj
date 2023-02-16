import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cur = 1
op = []
isValid = True
q = deque()

for _ in range(n):
    num = int(input())
    while(cur<=num):
        q.append(cur)
        cur+=1
        op.append('+')
    if q[-1]==num:
        q.pop()
        op.append('-')
    else:
        isValid = False
        break

if isValid:
    for i in op:
        print(i)
else:
    print('NO')

    