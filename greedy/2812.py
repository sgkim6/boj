from collections import deque

N, K = map(int,input().split())
max_len = N-K

q = deque(input())
answer = deque()

while(q):
    if len(answer) == 0:
        answer.append(q.popleft())
    else:
        if q[0]<=answer[-1] or K==0:
            if len(answer)<max_len:
                answer.append(q.popleft())
            else:
                q.popleft()
        else:
            answer.pop()
            K-=1

result = ''.join(answer)
print(result)