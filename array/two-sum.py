"""
https://leetcode.com/problems/two-sum/solution/ 
"""


def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return "No two sum solution"


def two_sum_two_pass_hashtable(nums, target):
    hashtable = {}
    for i in range(len(nums)):
        hashtable[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashtable and hashtable.get(complement) != i:
            return [i, hashtable.get(complement)]
    return "No two sum solution"


def two_sum_one_pass_hashtable(nums, target):
    hashtable = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashtable:
            return [hashtable.get(complement), i]
        hashtable[nums[i]] = i
    return "No two sum solution"


nums = [2, 7, 11, 15]
target = 9
print("Two sum brute force")
print(two_sum_brute_force(nums, target))
print("Two sum two-pass hash table")
print(two_sum_two_pass_hashtable(nums, target))
print("Two sum one-pass hash table")
print(two_sum_one_pass_hashtable(nums, target))

nums = [3, 2, 4]
target = 6
print("Two sum brute force")
print(two_sum_brute_force(nums, target))
print("Two sum two-pass hash table")
print(two_sum_two_pass_hashtable(nums, target))
print("Two sum one-pass hash table")
print(two_sum_one_pass_hashtable(nums, target))

nums = [3, 3]
target = 6
print("Two sum brute force")
print(two_sum_brute_force(nums, target))
print("Two sum two-pass hash table")
print(two_sum_two_pass_hashtable(nums, target))
print("Two sum one-pass hash table")
print(two_sum_one_pass_hashtable(nums, target))
