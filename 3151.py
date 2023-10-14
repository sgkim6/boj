from bisect import bisect_left

N = int(input())

students = sorted(list(map(int, input().split())))

answer = 0


for start in range(0, N-2):
    mid = start + 1
    end = N-1
    while mid < end:
        sum_of_score = students[start] + students[mid] + students[end]
        if sum_of_score == 0:
            if students[mid] == students[end]:
                answer += end - mid
            else:
                answer += end - bisect_left(students, students[end]) + 1
            mid += 1
        elif sum_of_score < 0:
            mid += 1
        else:
            end -= 1

print(answer)
