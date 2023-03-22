N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

answer = []

while (start <= end):
    mid = (start + end) // 2
    count = 0
    for tree in trees:
        if tree > mid:
            count += tree-mid

    if count < M:  # 부족
        start = mid+1
    elif count > M:  # 많음
        end = mid-1
        answer.append(count)
    else:
