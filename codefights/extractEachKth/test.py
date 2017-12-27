def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray


def extractEachKth(inputArray, k):
    return [i for (n,i) in enumerate(inputArray) if (n+1) % k != 0]


# test
inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3

# test
inputArray = [1, 1, 1, 1, 1]
k = 1

# test
inputArray = [1, 2, 1, 2, 1, 2, 1, 2]
k = 2
