import sys
input = sys.stdin.readline

N = int(input())

info = []
prev_x, prev_y = map(int, input().split())

count = 0
up = 0
down = 0

for _ in range(N-1):

    cur_x, cur_y = map(int, input().split())

    if (prev_y < 0 and cur_y > 0):
        up = cur_x
        prev_y = cur_y
    elif (prev_y > 0 and cur_y < 0):
        down = cur_x
        prev_y = cur_y
        if (up < down):
            info.append((up, down))
        else:
            info.append((down, up))

not_covered = len(info)
not_covering = 0
visited = [False]*len(info)

info.sort(key=lambda x: x[0])
info.append((99999999999, 99999999999))

for i in range(len(info)-1):
    # checkLoop = False
    left = info[i][0]
    right = info[i][1]

    if (right < info[i+1][0]):
        not_covering += 1
        continue

    for j in range(i+1, len(info)):
        # if (checkLoop == True):
        #     continue
        # if (checkLoop == False):
        if info[j][0] < right and (visited[j] == False):
            # if visited[i] == False:
            #     visited[i] = True
            #     not_covering -= 1
            visited[j] = True
            not_covered -= 1
        # else:
        #     checkLoop = True
        #     continue
print(not_covered, not_covering)
