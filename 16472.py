import sys
from collections import deque, defaultdict

N = int(input())

string = input()

start = 0
end = 1
answer = 0
tmp = 0

charset = set()
counter = defaultdict(int)

while (end <= len(string)):
    charset.add(string[end-1])
    counter[string[end-1]] += 1
    tmp += 1

    if (len(charset) <= N):
        pass
    else:
        cur = string[start]  # 현재 가장 앞의 문자
        while (len(charset) > N):
            tmp -= 1
            counter[string[start]] -= 1
            if (counter[string[start]] == 0):
                charset.remove(string[start])
            start += 1

    end += 1
    answer = max(answer, tmp)
print(answer)
