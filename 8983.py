import heapq

M, N, L = map(int, input().split())

lanes = list(map(int, input().split()))  # 사로들

heapq.heapify(lanes)

left = -99999999999
answer = 0

animals = []  # 동물들


def check(x, y, shooter, L):  # 맨해튼 거리 체크하는
    return abs(x - shooter) + y <= L


for i in range(N):
    x, y = map(int, input().split())
    heapq.heappush(animals, (x, y))

while animals:
    x, y = heapq.heappop(animals)  # 동물 좌표 가져옴

    while lanes:  # 동물보다 왼쪽에 있는 사로 중 가장 동물에 가까운 사로 left에 저장
        if lanes[0] <= x:
            left = heapq.heappop(lanes)
        else:
            break

    if not lanes:  # 만약 동물이 맨 오른쪽 사로보다 오른쪽에 위치 할 경우
        if check(x, y, left, L):
            answer += 1
        continue

    if check(x, y, left, L):  # 만약 동물의 왼쪽 사로보다
        answer += 1
        continue

    if check(x, y, lanes[0], L):
        answer += 1
        continue

print(answer)
