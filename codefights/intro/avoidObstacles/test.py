def avoidObstacles(inputArray):

    # Method 1
    # c represents the min length to jump
    c = 2
    while True:
        # i%c > 0 means no i was landed on the jump
        if sorted([i % c for i in inputArray])[0] > 0:
            return c
        c += 1

    # # Method 2
    # i=2
    # while True:
    #   if all(x%i!=0 for x in inputArray):
    #     return i
    #   i=i+1


inputArray = [5, 3, 6, 7, 9]
print(avoidObstacles(inputArray))
inputArray = [2, 3]
print(avoidObstacles(inputArray))
inputArray = [1, 4, 10, 6, 2]
print(avoidObstacles(inputArray))
