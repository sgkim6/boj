N = int(input())

string = input()

w_deque = []
e_deque = []

answer = 0
w_count = 0
e_count = 0

for i in range(N):
    if string[i] == 'W':
        w_count += 1
    if string[i] == 'H':
        w_deque.append(w_count)

for i in range(N-1, -1, -1):
    if string[i] == 'E':
        e_count += 1
    if string[i] == 'H':
        e_deque.append(e_count)

for i in range(len(w_deque)):
    tmp = w_deque[i] * ((2**e_deque[-i-1]) - e_deque[-i-1] - 1)
    answer += tmp

print(answer % 1000000007)
