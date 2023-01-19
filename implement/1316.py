n = int(input())
L = []
result = 0
for i in range(n):
    s = input()
    L.append(s)


def checkStr(s):
    checkList = [0]*26
    last_word = ''
    for i in range(len(s)):
        if checkList[ord(s[i])-97] != 0 and last_word != s[i]:
            return False
        last_word = s[i]
        checkList[ord(s[i])-97] = 1
    return True


for i in L:
    if checkStr(i):
        result += 1

print(result)
