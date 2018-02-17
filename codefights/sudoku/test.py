import numpy as np
# Method 1
def sudoku(grid):
    rows = np.array(grid)
    columns = rows.transpose()
    matrixes = rows.reshape((3,3,3,3)).transpose((0,2,1,3)).reshape((9,9))

    def unique(arrays):
        count = 0
        for array in arrays:
            if len(array) > len(set(array)):
                count += 1
                return count

    counts = unique(rows) + unique(columns) + unique(matrixes)
    if counts == 0:
        return True
    else:
        return False

# Method 2
def sudoku(grid):

    def r(i):
        return sorted(grid[i]) != list(range(1,10))

    def c(i):
        return sorted([grid[x][i] for x in range(9)]) != list(range(1,10))

    def g(x,y):
        return sorted([grid[i][j] for i in range(x,x+3) for j in range(y,y+3)]) != list(range(1,10))

    for i in range(9):
        if r(i) or c(i):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if g(i,j):
                return False
    return True


# Unit test
grid = [[1,3,2,5,4,6,9,8,7],
 [4,6,5,8,7,9,3,2,1],
 [7,9,8,2,1,3,6,5,4],
 [9,2,1,4,3,5,8,7,6],
 [3,5,4,7,6,8,2,1,9],
 [6,8,7,1,9,2,5,4,3],
 [5,7,6,9,8,1,4,3,2],
 [2,4,3,6,5,7,1,9,8],
 [8,1,9,3,2,4,7,6,5]]
print(sudoku(grid))
# Expected Output = true

# Unit test
grid = [[1,3,2,5,4,6,9,2,7],
 [4,6,5,8,7,9,3,8,1],
 [7,9,8,2,1,3,6,5,4],
 [9,2,1,4,3,5,8,7,6],
 [3,5,4,7,6,8,2,1,9],
 [6,8,7,1,9,2,5,4,3],
 [5,7,6,9,8,1,4,3,2],
 [2,4,3,6,5,7,1,9,8],
 [8,1,9,3,2,4,7,6,5]]
print(sudoku(grid))
# Expected Output = false

# Unit test
grid = [[1,3,4,2,5,6,9,8,7],
 [4,6,8,5,7,9,3,2,1],
 [7,9,2,8,1,3,6,5,4],
 [9,2,3,1,4,5,8,7,6],
 [3,5,7,4,6,8,2,1,9],
 [6,8,1,7,9,2,5,4,3],
 [5,7,6,9,8,1,4,3,2],
 [2,4,5,6,3,7,1,9,8],
 [8,1,9,3,2,4,7,6,5]]
print(sudoku(grid))
# Expected Output = false

# Unit test
grid = [[1,3,2,5,4,6,9,8,7],
 [4,6,5,8,7,9,3,2,1],
 [7,9,8,2,1,3,6,5,4],
 [9,2,1,4,3,5,8,7,6],
 [3,5,4,7,6,8,2,1,9],
 [6,8,7,1,9,2,5,4,3],
 [5,4,6,9,8,1,4,3,2],
 [2,7,3,6,5,7,1,9,8],
 [8,1,9,3,2,4,7,6,5]]
print(sudoku(grid))
# Expected Output = false

# Unit test
grid = [[1,2,3,4,5,6,7,8,9],
 [4,6,5,8,7,9,3,2,1],
 [7,9,8,2,1,3,6,5,4],
 [1,2,3,4,5,6,7,8,9],
 [4,6,5,8,7,9,3,2,1],
 [7,9,8,2,1,3,6,5,4],
 [1,2,3,4,5,6,7,8,9],
 [4,6,5,8,7,9,3,2,1],
 [7,9,8,2,1,3,6,5,4]]
print(sudoku(grid))
# Expected Output = false

# Unit test
grid = [[5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,8],
 [1,9,8,3,4,2,5,6,7],
 [8,5,9,9,6,1,4,2,3],
 [4,2,6,8,5,3,7,9,1],
 [7,1,3,7,2,4,8,5,6],
 [9,6,1,5,3,7,2,8,4],
 [2,8,7,4,1,9,6,3,5],
 [3,4,5,2,8,6,1,7,9]]
print(sudoku(grid))
# Expected Output = false

# Unit test
grid = [[5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5]]
print(sudoku(grid))
# Expected Output = false
