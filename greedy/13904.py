import sys
input = sys.stdin.readline
import heapq

N = int(input())


arr = []
heap = []
answer = []

for _ in range(N):
    d, w = map(int,input().split())
    heapq.heappush(arr,(-d,-w))


day = -min(arr)[0]

while(day>0):
    while arr:
        if(-arr[0][0]==day):
            tmp = heapq.heappop(arr)
            heapq.heappush(heap,(tmp[1],tmp[0]))
        else:
            break
    if heap:
        value = heapq.heappop(heap)[0]
        answer.append(-value)
    day -= 1
    

print(sum(answer))
