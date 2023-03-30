# def checkSudoku(M):
#     for i in range(9):
#         row_arr = [0] * 10
#         col_arr = [0] * 10
#         for j in range(9):
#             row = M[i][j]
#             col = M[j][i]

#             if row_arr[row]:
#                 return 0
#             if col_arr[col]:
#                 return 0

#             row_arr[row] = 1
#             col_arr[col] = 1

#             if i % 3 == 0 and j % 3 == 0:
#                 square = [0] * 10
#                 for r in range(i, i+3):
#                     for c in range(j, j+3):
#                         num = M[r][c]
#                         if square[num]:
#                             return 0
#                         square[num] = 1

#     return 1


# T = int(input())
# for test_case in range(1, T+1):
#     mat = [list(map(int, input().split())) for _ in range(9)]

#     result = checkSudoku(mat)

#     print(f'#{test_case} {result}')

print(*[1, 3, 4, 5, 5], sep='\n')
