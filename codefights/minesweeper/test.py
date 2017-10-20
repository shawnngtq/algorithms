# Step by step method
def minesweeper(matrix):
  nrow = len(matrix)
  ncol = len(matrix[0])
  m = [[0 for j in range(ncol)] for i in range(nrow)]
  
  for i in range(nrow):
    for j in range(ncol):
      # Top left
      if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1]:
        m[i][j] += 1
      # Top
      if j-1 >= 0 and matrix[i][j-1]:
        m[i][j] += 1
      # Top right
      if i+1 < len(matrix) and j > 0 and matrix[i+1][j-1]:
        m[i][j] += 1
      # Left
      if i-1 >= 0 and matrix[i-1][j]:
        m[i][j] += 1
      # Right
      if i+1 < len(matrix) and matrix[i+1][j]:
        m[i][j] += 1
      # Bottom left
      if i-1 >= 0 and j+1 < len(matrix[i]) and matrix[i-1][j+1]:
        m[i][j] += 1
      # Bottom
      if j+1 < len(matrix[i]) and matrix[i][j+1]:
        m[i][j] += 1
      # Bottom right
      if i+1 < len(matrix) and j+1 < len(matrix[i]) and matrix[i+1][j+1]:
        m[i][j] += 1
  return m


def minesweeper(matrix):
  nrow = len(matrix)
  ncol = len(matrix[0])
  m = [[0 for j in range(ncol)] for i in range(nrow)]
  
  for i in range(nrow):
    for j in range(ncol):
      # Top left
      if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1]:
        m[i][j] += 1
      # Top
      if j-1 >= 0 and matrix[i][j-1]:
        m[i][j] += 1
      # Top right
      if i+1 < len(matrix) and j > 0 and matrix[i+1][j-1]:
        m[i][j] += 1
      # Left
      if i-1 >= 0 and matrix[i-1][j]:
        m[i][j] += 1
      # Right
      if i+1 < len(matrix) and matrix[i+1][j]:
        m[i][j] += 1
      # Bottom left
      if i-1 >= 0 and j+1 < len(matrix[i]) and matrix[i-1][j+1]:
        m[i][j] += 1
      # Bottom
      if j+1 < len(matrix[i]) and matrix[i][j+1]:
        m[i][j] += 1
      # Bottom right
      if i+1 < len(matrix) and j+1 < len(matrix[i]) and matrix[i+1][j+1]:
        m[i][j] += 1
  return m


# test 1
matrix = [[True,False,False], 
 [False,True,False], 
 [False,False,False]]
print(minesweeper(matrix))
# test 2
matrix = [[False,False,False], 
 [False,False,False]]
print(minesweeper(matrix))
# test 3
matrix = [[True,False,False,True], 
 [False,False,True,False], 
 [True,True,False,True]]
print(minesweeper(matrix))