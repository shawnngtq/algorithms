def chessKnight(cell):
    row = ord(cell[1]) - ord('0')
    column = ord(cell[0]) - ord('a') + 1
    steps = [[-2, 1],[-2, -1],[-1, 2],[-1, -2],[1, 2],[1, -2],[2, 1],[2, -1]]

    answer = 0
    for i in range(len(steps)):
        tmpRow = row + steps[i][0]
        tmpColumn =  column + steps[i][1] 
        if (1 <= tmpRow <= 8 and 1 <= tmpColumn <= 8):
            answer += 1

    return answer


def chessKnight(cell):
    row = 0
    column = [ord(cell[0])-96,int(cell[1])]

    moves = [[1,2],[2,1],[1,-2],[-2,1],[-1,2],[2,-1],[-1,-2],[-2,-1]]

    for i in moves:
        if 0<column[0]+i[0]<9 and 0<column[1]+i[1]<9:
            row +=1
    return row


# test
cell = "a1"
print(chessKnight(cell))

# test
cell = "c2"
print(chessKnight(cell))

# test
cell = "d4"
print(chessKnight(cell))

# test
cell = "g6"
print(chessKnight(cell))
