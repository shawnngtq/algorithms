# Method 1
def spiralNumbers(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m


# Method 2
def spiralNumbers(n):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    matrix = [[0 for i in range(n)] for i in range(n)]
    current_pos = (0, 0)
    current_dir = 0
    for i in range(1, n * n + 1):
        matrix[current_pos[0]][current_pos[1]] = i
        next_pos = (
            current_pos[0] + direction[current_dir][0],
            current_pos[1] + direction[current_dir][1],
        )
        if (
            next_pos[0] >= n
            or next_pos[0] < 0
            or next_pos[1] >= n
            or next_pos[1] < 0
            or matrix[next_pos[0]][next_pos[1]] != 0
        ):
            current_dir = (current_dir + 1) % 4
            next_pos = (
                current_pos[0] + direction[current_dir][0],
                current_pos[1] + direction[current_dir][1],
            )
        current_pos = next_pos
    return matrix


# Unit test
n = 3
print(spiralNumbers(n))
# Expected Output = [[1,2,3],
#  [8,9,4],
#  [7,6,5]]

# Unit test
n = 5
print(spiralNumbers(n))
# Expected Output = [[1,2,3,4,5],
#  [16,17,18,19,6],
#  [15,24,25,20,7],
#  [14,23,22,21,8],
#  [13,12,11,10,9]]

# Unit test
n = 6
print(spiralNumbers(n))
# Expected Output = [[1,2,3,4,5,6],
#  [20,21,22,23,24,7],
#  [19,32,33,34,25,8],
#  [18,31,36,35,26,9],
#  [17,30,29,28,27,10],
#  [16,15,14,13,12,11]]

# Unit test
n = 7
print(spiralNumbers(n))
# Expected Output = [[1,2,3,4,5,6,7],
#  [24,25,26,27,28,29,8],
#  [23,40,41,42,43,30,9],
#  [22,39,48,49,44,31,10],
#  [21,38,47,46,45,32,11],
#  [20,37,36,35,34,33,12],
#  [19,18,17,16,15,14,13]]

# Unit test
n = 10
print(spiralNumbers(n))
# Expected Output = [[1,2,3,4,5,6,7,8,9,10],
#  [36,37,38,39,40,41,42,43,44,11],
#  [35,64,65,66,67,68,69,70,45,12],
#  [34,63,84,85,86,87,88,71,46,13],
#  [33,62,83,96,97,98,89,72,47,14],
#  [32,61,82,95,100,99,90,73,48,15],
#  [31,60,81,94,93,92,91,74,49,16],
#  [30,59,80,79,78,77,76,75,50,17],
#  [29,58,57,56,55,54,53,52,51,18],
#  [28,27,26,25,24,23,22,21,20,19]]
