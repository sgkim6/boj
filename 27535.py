H, T, C, K, G = map(int, input().split())

chocolates = [
    ['H', H],
    ['T', T],
    ['C', C],
    ['K', K],
    ['G', G]
]

alphabet = ['H', 'T', 'C', 'K', 'G']

M = int(input())
base = 10
chocolates_sum = H+T+C+K+G

if chocolates_sum > 0:
    base = chocolates_sum % 10
    if base == 1 or base == 0:
        base = 10
else:
    base = 1

for _ in range(M):
    eat = list(map(int, input().split()))
    for i in range(5):
        for j in range(5):
            if chocolates[j][0] == alphabet[i]:
                chocolates[j][1] -= eat[i]
                chocolates_sum -= eat[i]

# -----------진법 변환---------------
    q, r = divmod(chocolates_sum, base)

    char = ""

    while(q != 0):
        char = str(r) + char
        q, r = divmod(q, base)

    char = str(r) + char
# --------------------------------------

    chocolates.sort(key=lambda x: (-x[1], x[0]))

    result = ""

    if chocolates_sum != 0:
        for chocolate in chocolates:
            if chocolate[1] != 0:
                result = result + chocolate[0]
    else:
        result = "NULL"

    print(f"{char}7H")
    print(result)

    if chocolates_sum > 0:
        base = chocolates_sum % 10
        if base == 1 or base == 0:
            base = 10
    else:
        base = 1
