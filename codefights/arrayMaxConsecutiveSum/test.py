def arrayMaxConsecutiveSum(inputArray, k):
    c = m = sum(inputArray[:k])
    
    for i in range(len(inputArray) - k):
        c = c + inputArray[i + k] - inputArray[i]
        m = max(c, m)
        
    return m


# test
inputArray = [2, 3, 5, 1, 6]
k = 2
print(arrayMaxConsecutiveSum(inputArray, k))

# test
inputArray = [2, 4, 10, 1]
k = 2
print(arrayMaxConsecutiveSum(inputArray, k))

# test
inputArray = [1, 3, 2, 4]
k = 3
print(arrayMaxConsecutiveSum(inputArray, k))

# test
inputArray = [3, 2, 1, 1]
k = 1
print(arrayMaxConsecutiveSum(inputArray, k))
