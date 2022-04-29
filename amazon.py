# https://www.educative.io/blog/crack-amazon-coding-interview-questions
def find_missing(input):
    sum_of_elements = sum(input)

    # There is exactly 1 number missing
    n = len(input) + 1
    actual_sum = (n * (n + 1)) / 2
    return actual_sum - sum_of_elements


input = [3, 7, 1, 2, 8, 4, 5]
print(find_missing(input))


def find_missing(arr):
    maximum = max(arr)
    missing = sum(range(1, maximum + 1)) - sum(arr)
    return missing


arr = [1, 2, 4, 5]
print(find_missing(arr))
arr = [3, 7, 1, 2, 8, 4, 5]
print(find_missing(arr))


def sum_of_two_int_equals_provided(arr, integer):
    table = {}
    for i in range(len(arr) - 1):
        total = arr[i] + arr[i + 1]
        if total not in table:
            table[total] = 1
        else:
            table[total] += 1
    if integer in table.keys():
        return True
    else:
        return False


arr = [5, 7, 1, 2, 8, 4, 3]
print(sum_of_two_int_equals_provided(arr, 10))
print(sum_of_two_int_equals_provided(arr, 19))


# assumption
class LinkedList:
    def __init__(self, data, next):
        self.data = data
        self.next = None


def merge_two_sorted_linked_list(ll1, ll2):
    new_ll = LinkedList(data=0)
    ref_ll = new_ll

    while ll1 or ll2:
        if ll1.data <= ll2.data:
            ref_ll.next = ll1.data
            ref_ll = ref_ll.next
            ll1 = ll1.next
        else:
            ref_ll.next = ll2.data
            ref_ll = ref_ll.next
            ll2 = ll2.next

    new_ll = new_ll.next
    return new_ll


ll1 = [4, 8, 15, 19]
ll2 = [7, 9, 10, 16]


# https://aonecode.com/amazon-online-assessment-questions
def movies_on_flight(arr, integer):
    table = {}
    for i in range(len(arr) - 1):
        total = arr[i] + arr[i + 1]
        if total < integer:
            if total not in table:
                table[total] = [arr[i], arr[i + 1]]
            else:
                table[total] += [arr[i], arr[i + 1]]

    print(table)
    return max(table, key=table.get)


def movies_on_flight(arr, integer):
    table = {}
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            total = arr[i] + arr[j]
            if total < integer:
                if total not in table:
                    table[total] = [arr[i], arr[j]]
                else:
                    table[total] += [arr[i], arr[j]]

    print(table)
    return max(table, key=table.get)


arr = [90, 85, 75, 60, 120, 150, 125]
print(movies_on_flight(arr, 250))
