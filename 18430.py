N, M = map(int, input().split())

graph = []
visited = [[False for i in range(M)] for j in range(N)]

for i in range(N):
    graph.append(list(map(int, input().split())))

offset = [[(0, 0), (0, 1), (-1, 0)],  # ㄴ
          [(0, 0), (0, 1), (1, 0)],  # r
          [(0, 0), (1, 0), (0, -1)],  # ㄱ
          [(0, 0), (0, -1), (-1, 0)]]  # J

answer = 0


def dfs(row, col, power):
    global answer

    c_row = row
    c_col = col
    c_power = power

    if c_col >= M:
        c_col = 0
        c_row += 1

    if c_row >= N:
        answer = max(c_power, answer)
        return

    for i in range(4):  # 각 방향으로 부메랑 만들기
        add_power = 0
        check = True

        for j in range(3):
            if c_col + offset[i][j][1] < 0 or M <= c_col + offset[i][j][1] or c_row + offset[i][j][0] < 0 or c_row + offset[i][j][0] >= M:
                check = False
                break
            if visited[c_row + offset[i][j][0]][c_col + offset[i][j][1]]:
                check = False
                break

            if j == 0:
                add_power += 2 * graph[c_row + offset[i]
                                       [j][0]][c_col + offset[i][j][1]]
            else:
                add_power += graph[c_row + offset[i]
                                   [j][0]][c_col + offset[i][j][1]]

        if check:
            for j in range(3):
                visited[c_row + offset[i][j][0]
                        ][c_col + offset[i][j][1]] = True

            dfs(c_row, c_col+1, c_power + add_power)

            visited[c_row + offset[i][j][0]
                    ][c_col + offset[i][j][1]] = False

        dfs(c_row, c_col+1, c_power)


dfs(0, 0, 0)
dfs(0, 1, 0)
dfs(1, 0, 0)
dfs(1, 1, 0)

print(answer)
