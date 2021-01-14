n = int(input())

listControl = ['L', 'R', 'U', 'D']
listX = [0, 0, -1, 1]
listY = [-1, 1, 0, 0]
x, y = 1, 1

listInput = list(map(str, input().split()))
for i in range(len(listInput)):
    idx = listControl.index(listInput[i])
    chgX = x + listX[idx]
    chgY = y + listY[idx]
    if chgX<1 or chgY<1 or chgX>n or chgY>n:
        continue
    else:
        x = chgX
        y = chgY
        print(x, y)
print(x, y)

