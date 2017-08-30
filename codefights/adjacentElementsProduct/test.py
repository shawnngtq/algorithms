def adjacentElementsProduct(inputArray):
  # method 1
  return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

  # method 2
  # return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))

inputArray = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray))
inputArray = [-1, -2]
print(adjacentElementsProduct(inputArray))
inputArray = [5, 1, 2, 3, 1, 4]
print(adjacentElementsProduct(inputArray))
inputArray = [1, 2, 3, 0]
print(adjacentElementsProduct(inputArray))
inputArray = [9, 5, 10, 2, 24, -1, -48]
print(adjacentElementsProduct(inputArray))
inputArray = [5, 6, -4, 2, 3, 2, -23]
print(adjacentElementsProduct(inputArray))
inputArray = [4, 1, 2, 3, 1, 5]
print(adjacentElementsProduct(inputArray))
inputArray = [-23, 4, -3, 8, -12]
print(adjacentElementsProduct(inputArray))
inputArray = [1, 0, 1, 0, 1000]
print(adjacentElementsProduct(inputArray))