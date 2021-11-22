def bishopAndPawn(bishop, pawn):
    bishop = [ord(bishop[0]), int(bishop[1])]
    pawn = [ord(pawn[0]), int(pawn[1])]
    return bishop[1] - bishop[0] == pawn[1] - pawn[0] or sum(bishop) == sum(pawn)


def bishopAndPawn(bishop, pawn):
    return abs((ord(pawn[0]) - ord(bishop[0])) / (int(pawn[1]) - int(bishop[1]))) == 1


def bishopAndPawn(bishop, pawn):
    return (ord(bishop[0]) + int(bishop[1]) == ord(pawn[0]) + int(pawn[1])) or (
        ord(bishop[0]) + int(pawn[1]) == ord(pawn[0]) + int(bishop[1])
    )


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
