N = int(input())
cranes = list(map(int, input().split()))

M = int(input())
boxs = list(map(int, input().split()))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

if boxs[0] > cranes[0]: #가장 큰 박스를 들 수 없으면 -1
    print(-1)
else:
    answer = 0

    while boxs: #box 남아있는 동안
        for crane in cranes:
            for box in boxs:
                if crane >= box: #크레인이 박스를 들 수 있으면
                    boxs.remove(box) #박스 제거
                    break

        answer += 1 #모든 크레인 순회하고 시간+1

    print(answer)