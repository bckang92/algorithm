full = input()

col = full[0]
row = int(full[1])

colSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rowSet = [1, 2, 3, 4, 5, 6, 7, 8]

colMove = [-2, -1, 1, 2, 2, 1, -1, -2]
rowMove = [-1, -2, -2, -1, 1, 2, 2, 1]

colPos = colSet.index(col)
rowPos = rowSet.index(row)

result = 0

for i in range(8):
    tempCol = colPos + colMove[i]
    tempRow = rowPos + rowMove[i]
    if (-1 < tempCol < 8) and (-1 < tempRow < 8):
        result += 1

print(result)