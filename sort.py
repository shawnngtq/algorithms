def bubble_sort(list_):
    """
    compare 2 values every time
    """
    for i in range(len(list_)):
        for j in range(len(list_) - 1):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_


print(bubble_sort([4, 3, 2, 10, 12, 1, 5, 6]))


def bubble_sort(list_):
    for i in range(len(list_) - 1):
        for j in range(len(list_) - i - 1):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_


print(bubble_sort([4, 3, 2, 10, 12, 1, 5, 6]))


def selection_sort(list_):
    """
    using index & pointer, swap value accordingly
    """
    for i in range(len(list_)):
        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:
                min_index = j
        list_[i], list_[min_index] = list_[min_index], list_[i]
    return list_


print(selection_sort([4, 3, 2, 10, 12, 1, 5, 6]))


def insertion_sort(list_):
    for i in range(1, len(list_)):
        if list_[i] < list_[0]:
            value = list_.pop(i)
            list_.insert(0, value)
        else:
            for j in range(1, i):
                if list_[i] < list_[j]:
                    value = list_.pop(i)
                    list_.insert(j, value)
    return list_


print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))


def insertion_sort(list_):
    for i in range(1, len(list_)):
        for j in range(i):
            if list_[i] < list_[j]:
                list_.insert(j, list_.pop(i))
    return list_


print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        value = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than value, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr


print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))


def merge_sort(list_):
    """
    split list using divide and conquer, then merge based on ascending value
    """

    def merge(list1, list2):
        list1 = sorted(list1)
        list2 = sorted(list2)

    return


print(merge_sort([4, 3, 2, 10, 12, 1, 5, 6]))
