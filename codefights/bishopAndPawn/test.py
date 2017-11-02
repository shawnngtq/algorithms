def bishopAndPawn(b, p):
    b=[ord(b[0]),int(b[1])]
    p=[ord(p[0]),int(p[1])]
    return b[1]-b[0]==p[1]-p[0] or sum(b)==sum(p)


def bishopAndPawn(bishop, pawn):
    return abs((ord(pawn[0])-ord(bishop[0]))/(int(pawn[1])-int(bishop[1]))) == 1


def bishopAndPawn(bishop, pawn):
    return (ord(bishop[0]) + int(bishop[1]) == ord(pawn[0]) + int(pawn[1])) or (ord(bishop[0]) + int(pawn[1]) == ord(pawn[0]) + int(bishop[1]))


# test
bishop = "a1"
pawn = "c3"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "h1"
pawn = "h3"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "a5"
pawn = "c3"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "g1"
pawn = "f3"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "e7"
pawn = "d6"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "e7"
pawn = "a3"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "e3"
pawn = "a7"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "a1"
pawn = "h8"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "a1"
pawn = "h7"
print(bishopAndPawn(bishop, pawn))

# test
bishop = "h1"
pawn = "a8"
print(bishopAndPawn(bishop, pawn))
