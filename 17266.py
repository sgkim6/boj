N = int(input())
M = int(input())
points = list(map(int, input().split()))
answer = 0
for i in range(1, M):
    answer = max(answer, (points[i] - points[i-1])//2)
print(max(answer, points[0], N-points[-1]))
