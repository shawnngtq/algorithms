# Recursive method, O(2^n)
# Returns minimum value of the difference of two subsets
def findMinDiff(array, n):
    # Compute total sum of elements
    totalSum = 0
    for i in range(n):
        totalSum += array[i]

    # Compute result using recursive function
    return findMinSum(array, n, 0, totalSum)


# Function to find the minimum sum
def findMinSum(array, i, subset1Sum, totalSum):

    # When we reached the last element
    # return the absolute value of difference between
    # subset 1 and subset 2 sum
    subset2Sum = totalSum - subset1Sum
    if i == 0:
        return abs(subset2Sum - subset1Sum)

    # For every item array[i], 2 choices
    # 1) Include in subset 1
    # 2) Include in subset 2
    # return the minimum of 2 choices
    minimum = min(
        findMinSum(array, i - 1, subset1Sum + array[i - 1], totalSum),
        findMinSum(array, i - 1, subset1Sum, totalSum),
    )

    return minimum


array = [3, 1, 4, 2, 2, 1]
n = len(array)
print("The minimum difference between 2 sets is:", findMinDiff(array, n))

array = [1, 6, 11, 5]
n = len(array)
print("The minimum difference between 2 sets is:", findMinDiff(array, n))


# Tabulation, O(n^sum)
def findMinDiffDP(array, n):
    totalSum = 0
    for i in range(n):
        totalSum += array[i]

    table = [[None] * (totalSum + 1) for i in range(n + 1)]

    # Initialize 1st col as True
    for i in range(n + 1):
        table[i][0] = True

    # Initialize 1st row, except table[0][0] as False
    for j in range(1, totalSum + 1):
        table[0][j] = False

    # Tabulation
    for i in range(1, n + 1):
        for j in range(1, totalSum + 1):
            # If ith element is excluded
            table[i][j] = table[i - 1][j]
            # If ith element is included
            if array[i - 1] <= j:
                table[i][j] |= table[i - 1][j - array[i - 1]]

    # Find the largest j such that table[n][j] is true
    # where j loops from totalSum/2 to 0
    for j in range(int(totalSum / 2), 0, -1):
        if table[n][j] == True:
            diff = totalSum - (2 * j)
            break

    return diff


array = [3, 1, 4, 2, 2, 1]
n = len(array)
print("The minimum difference between 2 sets is:", findMinDiffDP(array, n))

array = [1, 6, 11, 5]
n = len(array)
print("The minimum difference between 2 sets is:", findMinDiffDP(array, n))
