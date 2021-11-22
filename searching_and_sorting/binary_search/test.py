# Recursive search, O(log n)
def binarySearch(array, left, right, x):
    # check base case
    if right >= left:
        mid = int(left + (right - left) / 2)

        # If element is present at the middle itself
        if x == array[mid]:
            return mid

        # If element is smaller than mid, then it can only be present at left side
        elif x < array[mid]:
            return binarySearch(array, left, mid - 1, x)

        # Else, element present in right subarray
        else:
            return binarySearch(array, mid + 1, right, x)

    else:
        # Element not present in array
        return -1


array = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(array, 0, len(array) - 1, x)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")


# Iterative search, O(log n)
def binarySearch(array, left, right, x):
    while left <= right:
        mid = int(left + (right - left) / 2)

        # if x is mid
        if x == array[mid]:
            return mid

        # if x is smaller, ignore right subset
        elif x < array[mid]:
            right = mid - 1

        # if x is bigger, ignore left subset
        else:
            left = mid + 1

    # if element not present
    return -1


array = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(array, 0, len(array) - 1, x)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
