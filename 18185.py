import math

N = int(input())

arr_input = list(map(int, input().split()))
arr2_input = list(reversed(arr_input))

# print(arr_input)
# print(arr2_input)


def find(arr):
    answer = 0
    for i in range(len(arr)-2):

        if (arr[i] == 0):
            continue

        if (arr[i+1] == 0):
            answer += (arr[i] * 3)
            arr[i] = 0
            continue

        if (arr[i+1] != 0):
            if (arr[i+2] == 0):
                tmp2 = min(arr[i], arr[i+1])
                answer += tmp2*5
                arr[i+1] -= tmp2
                arr[i] -= tmp2

                if arr[i] == 0:
                    continue
                else:
                    answer += arr[i]*3
                    arr[i] = 0
                    continue

        if (arr[i+2] != 0):
            while ((arr[i+1] > arr[i+2]) and (arr[i] > 0)):
                arr[i+1] -= 1
                arr[i] -= 1
                answer += 5

            if (arr[i] == 0):
                continue

            tmp3 = min(arr[i], arr[i+1], arr[i+2])
            answer += 7*tmp3
            arr[i] -= tmp3
            arr[i+1] -= tmp3
            arr[i+2] -= tmp3

            # case 1
            if (arr[i] == 0):
                continue
            if (arr[i+1] == 0):
                answer += arr[i]*3
                continue

            tmp = min(arr[i], arr[i+1])
            answer += tmp*5
            arr[i] -= tmp
            arr[i+1] -= tmp
            if (arr[i] == 0):
                continue
            answer += arr[i]*3
            arr[i] = 0

    if (arr[-2] == 0 or arr[-1] == 0):
        answer += arr[-2]*3
        answer += arr[-1]*3
    else:
        answer += min(arr[-2], arr[-1]) * 5
        answer += abs(arr[-2] - arr[-1]) * 3

    return answer

# for i in range(len(arr2)-2):
#     print(answer2)
#     if (arr2[i] == 0):
#         continue

#     if (arr2[i+1] == 0):
#         answer2 += (arr2[i] * 3)
#         arr2[i] = 0
#         continue

#     if (arr2[i+1] != 0):
#         if (arr2[i+2] == 0):
#             tmp2 = min(arr2[i], arr2[i+1])
#             answer2 += tmp2*5
#             arr2[i+1] -= tmp2
#             arr2[i] -= tmp2

#             if arr2[i] == 0:
#                 continue
#             else:
#                 answer2 += arr2[i]*3
#                 arr2[i] = 0
#                 continue

#     if (arr2[i+2] != 0):
#         if (arr[i+1] > max(arr[i], arr[i+2])):
#             answer += arr[i] * 5
#             arr[i+1] -= arr[i]
#             arr[i] = 0
#             continue
#         tmp3 = min(arr2[i], arr2[i+1], arr2[i+2])
#         answer2 += 7*tmp3
#         arr2[i] -= tmp3
#         arr2[i+1] -= tmp3
#         arr2[i+2] -= tmp3

#         # case 1
#         if (arr2[i] == 0):
#             continue
#         if (arr2[i+1] == 0):
#             answer2 += arr2[i]*3
#             continue

#         tmp = min(arr2[i], arr2[i+1])
#         answer2 += tmp*5
#         arr2[i] -= tmp
#         arr2[i+1] -= tmp
#         if (arr2[i] == 0):
#             continue
#         answer2 += arr2[i]*3
#         arr2[i] = 0

# if (arr2[-2] == 0 or arr2[-1] == 0):
#     answer2 += arr2[-2]*3
#     answer2 += arr2[-1]*3
# else:
#     answer2 += min(arr2[-2], arr2[-1]) * 5
#     answer2 += abs(arr2[-2] - arr2[-1]) * 3


print(min(find(arr_input), find(arr2_input)))
