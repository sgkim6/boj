T = int(input())

dx = [0, 1, 0, -1]  # 북, 동, 남, 서 0 1 2 3 4 5 6 ..-> 우회전
dy = [1, 0, -1, 0]                  


for test_case in range(1, T+1):
    cmd = input()
    direction = 0
    x = 0
    y = 0
    x_log = [0]
    y_log = [0]

    for i in cmd:
        if i == 'F':
            x += dx[direction]
            y += dy[direction]
            x_log.append(x)
            y_log.append(y)
        elif i == 'B':
            direction += 2
            direction = direction % 4
            x += dx[direction]
            y += dy[direction]
            direction += 2
            direction = direction % 4
            x_log.append(x)
            y_log.append(y)
        elif i == 'L':
            direction += 3
            direction = direction % 4
        elif i == 'R':
            direction += 1
            direction = direction % 4

    print((max(y_log)-min(y_log)) * (max(x_log)-min(x_log)))
