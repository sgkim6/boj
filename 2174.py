from collections import defaultdict

A, B = map(int, input().split())
N, M = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]  # 동 남 서 북

robot = {}  # x, y, dirr
graph = [[0 for i in range(B+1)] for j in range(A+1)]
crashed = False  # 종료조건 체크
answer = 'OK'

for i in range(N):
    x, y, dirr = input().split()
    x = int(x)
    y = int(y)

    if(dirr == 'E'):
        dirr = 0
    elif(dirr == 'S'):
        dirr = 1
    elif(dirr == 'W'):
        dirr = 2
    elif(dirr == 'N'):
        dirr = 3

    robot[i+1] = (x, y, dirr)
    graph[x][y] = i+1

for i in range(M):
    num, cmd, repeat = input().split()
    if crashed:
        continue

    num = int(num)
    repeat = int(repeat)

    x, y, dirr = robot[num]

    if cmd == 'F':
        for step in range(1, repeat+1):
            nx = x + dx[dirr] * step
            ny = y + dy[dirr] * step
            if nx <= 0 or nx > A or ny <= 0 or ny > B:
                crashed = True
                answer = f"Robot {num} crashes into the wall"
                break

            elif graph[nx][ny] != 0:
                crashed = True
                answer = f"Robot {num} crashes into robot {graph[nx][ny]}"
                break

        if not crashed:
            graph[x][y] = 0
            graph[nx][ny] = num
            robot[num] = (nx, ny, dirr)
    elif cmd == 'R':
        for step in range(repeat):
            dirr += 1
        dirr = dirr % 4
        robot[num] = (x, y, dirr)
    elif cmd == 'L':
        for step in range(repeat):
            dirr += 3
        dirr = dirr % 4
        robot[num] = (x, y, dirr)

print(answer)
