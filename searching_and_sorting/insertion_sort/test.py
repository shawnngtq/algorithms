# O(n*n)
def insertionSort(arr):
    n = len(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]

        # Move elements of arr[0.. i-1] that are
        # greater than key, to 1 position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))


# O(n^2)
# A binary search based function to find the position
# where x should be inserted in a[low..high]
def binarySearch(arr, left, right, x):
    if right <= left:
        return (left + 1) if (x > arr[left]) else left

    mid = int((left + right) / 2)

    if x == arr[mid]:
        return mid + 1

    if x > arr[mid]:
        return binarySearch(arr, mid + 1, right, x)
    return binarySearch(arr, left, mid - 1, x)


def binaryInsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        # find the location where key should be inserted
        location = binarySearch(arr, 0, j, key)
        while j >= location:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = [12, 11, 13, 5, 6]
print(binaryInsertionSort(arr))
