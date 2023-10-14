N = int(input())

snows = sorted(list(map(int, input().split())))

answer = int(1e10)

for anna_left in range(len(snows) - 3):
    for anna_right in range(anna_left + 3, len(snows)):
        anna_snowman = snows[anna_left] + snows[anna_right]
        elsa_left = anna_left + 1
        elsa_right = anna_right - 1
        while elsa_left < elsa_right:
            elsa_snowman = snows[elsa_left] + snows[elsa_right]
            answer = min(answer, abs(anna_snowman - elsa_snowman))
            if anna_snowman < elsa_snowman:
                elsa_right -= 1
            else:
                elsa_left += 1

print(answer)
