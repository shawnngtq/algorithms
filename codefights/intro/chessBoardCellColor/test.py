def chessBoardCellColor(cell1, cell2):
    darklist = []
    whitelist = []
    for i in range(1, 9):
        for j in range(ord("A"), ord("H") + 1):
            if i % 2 == 1:
                if j % 2 == 1:
                    darklist.append(chr(j) + str(i))
                else:
                    whitelist.append(chr(j) + str(i))
            if i % 2 == 0:
                if j % 2 == 1:
                    whitelist.append(chr(j) + str(i))
                else:
                    darklist.append(chr(j) + str(i))

    if all(x in whitelist for x in [cell1, cell2]):
        return True
    elif all(x in darklist for x in [cell1, cell2]):
        return True
    else:
        return False


def chessBoardCellColor(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0


# test
cell1 = "A1"
cell2 = "C3"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "A1"
cell2 = "H3"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "A1"
cell2 = "A2"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "A1"
cell2 = "B2"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "B3"
cell2 = "H8"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "C3"
cell2 = "B5"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "G5"
cell2 = "E7"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "C8"
cell2 = "H8"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "D2"
cell2 = "D2"
print(chessBoardCellColor(cell1, cell2))

# test
cell1 = "A2"
cell2 = "A5"
print(chessBoardCellColor(cell1, cell2))
