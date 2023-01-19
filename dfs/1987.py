# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
# 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸(1행 1열) 에는 말이 놓여 있다.

# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

from glob import glob
import sys

sys.setrecursionlimit(1000000000)

R, C = map(int, input().split())
L = []
result = 1
visit = set()

for i in range(R):
    s = sys.stdin.readline()
    L.append(s)


def dfs(x, y, cnt):
    global result
    if x < 0 or x >= R or y < 0 or y >= C:
        result = max(result, cnt)
        return False
    if L[x][y] not in visit:
        visit.add(L[x][y])
        cnt += 1
        if x < R-1:
            dfs(x+1, y, cnt)
        if x >= 1:
            dfs(x-1, y, cnt)
        if y < C-1:
            dfs(x, y+1, cnt)
        if y >= 1:
            dfs(x, y-1, cnt)
        visit.remove(L[x][y])
        return True
    else:
        result = max(result, cnt)
        return False


dfs(0, 0, 0)
print(result)
