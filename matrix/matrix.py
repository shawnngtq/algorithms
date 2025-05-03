matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate_90(matrix):
    # or 270 Degrees Counterclockwise
    return [list(row) for row in zip(*matrix[::-1])]


def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]


def rotate_270(matrix):
    # or 90 Degrees Counterclockwise
    return [list(row) for row in zip(*matrix)][::-1]


def top_left_to_bottom_right(matrix):
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []
    for d in range(rows + cols - 1):
        diag = []
        for i in range(max(0, d - cols + 1), min(rows, d + 1)):
            j = d - i
            diag.append(matrix[i][j])
        diagonals.append(diag)
    return diagonals


def top_right_to_bottom_left(matrix):
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []
    for d in range(-cols + 1, rows):
        diag = []
        for i in range(rows):
            j = i - d
            if 0 <= j < cols:
                diag.append(matrix[i][j])
        diagonals.append(diag)
    return diagonals


def bottom_left_to_top_right(matrix):
    diagonals = top_right_to_bottom_left(matrix)
    return [d[::-1] for d in diagonals]


def bottom_right_to_top_left(matrix):
    diagonals = top_left_to_bottom_right(matrix)
    return [d[::-1] for d in diagonals]


def zigzag_diagonal(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []

    for d in range(rows + cols - 1):
        temp = []
        r = 0 if d < cols else d - cols + 1
        c = d if d < cols else cols - 1

        while r < rows and c >= 0:
            temp.append(matrix[r][c])
            r += 1
            c -= 1

        if d % 2 == 0:
            result.extend(temp[::-1])
        else:
            result.extend(temp)

    return result


print(rotate_90(matrix))
print(rotate_180(matrix))
print(rotate_270(matrix))
print(top_left_to_bottom_right(matrix=matrix))
print(top_right_to_bottom_left(matrix=matrix))
print(bottom_left_to_top_right(matrix=matrix))
print(bottom_right_to_top_left(matrix=matrix))
print(zigzag_diagonal(matrix=matrix))
