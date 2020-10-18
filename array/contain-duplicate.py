"""
https://leetcode.com/problems/contains-duplicate/
"""


def contains_duplicate_naive_linear_search(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate_sorting(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False


def contains_duplicate_hashtable(nums):
    store = set()
    for item in nums:
        if item in store:
            return True
        store.add(item)
    return False


nums = [1, 2, 3, 1]
print("Contain duplcate naive linear search")
print(contains_duplicate_naive_linear_search(nums))
print("Contain duplicate sorting")
print(contains_duplicate_sorting(nums))
print("Contain duplicate hashtable")
print(contains_duplicate_hashtable(nums))

nums = [1, 2, 3, 4]
print("Contain duplcate naive linear search")
print(contains_duplicate_naive_linear_search(nums))
print("Contain duplicate sorting")
print(contains_duplicate_sorting(nums))
print("Contain duplicate hashtable")
print(contains_duplicate_hashtable(nums))

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print("Contain duplcate naive linear search")
print(contains_duplicate_naive_linear_search(nums))
print("Contain duplicate sorting")
print(contains_duplicate_sorting(nums))
print("Contain duplicate hashtable")
print(contains_duplicate_hashtable(nums))
