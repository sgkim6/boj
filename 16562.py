def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M, k = map(int, input().split())

answer = 0
parent = [0]
friends = []  # friends = (친구비, 친구 번호)
friend_set = set()  # 친구 그룹의 대표 set

for i in range(1, N+1):
    parent.append(i)

cost = list(map(int, input().split()))


for i in range(1, N+1):
    friends.append((cost[i-1], i))
friends.sort()  # 친구비가 싼 순으로 정렬

for i in range(M):
    a, b = map(int, input().split())
    union(a, b)

for friend in friends:  # 친구비가 싼 순으로 모든 친구 탐색
    top_friend = find(friend[1])  # top_friend = 뽑은 친구의 그룹 대표
    if top_friend not in friend_set:  # 그 대표가 나랑 안 친하면
        answer += friend[0]  # 친구비 내고
        friend_set.add(top_friend)  # 방금 뽑은 친구의 그룹 대표랑 친해짐

print(answer if answer <= k else "Oh no")
