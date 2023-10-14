n, W = map(int, input().split())
amount = 0
peak = False

graph = []

graph2 = []

for i in range(n):
    graph.append(int(input()))

for i in range(n-1):
    if not peak:
        if graph[i] < graph[i+1]:
            graph2.append(graph[i])
            peak = True

    if peak:
        if graph[i] > graph[i+1]:
            graph2.append(graph[i])
            peak = False

if peak:
    if graph[-2] < graph[-1]:
        graph2.append(graph[-1])

for i in range(len(graph2)):
    if i % 2 == 0:  # 매수 타이밍
        amount = W // graph2[i]  # 보유 코인량 증가
        if amount <= 0:
            continue
        W -= graph2[i] * amount  # 보유 금액 차감
    if i % 2 == 1:  # 매도 타이밍
        if amount <= 0:
            continue
        W += amount * graph2[i]
        amount = 0

print(W)
