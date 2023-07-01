from bisect import bisect_left
from bisect import bisect_right

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
inputs = list(map(int, input().split()))

cards.sort()
answer = []
for i in inputs:
    answer.append(bisect_right(cards, i) - bisect_left(cards, i))

print(*answer)
