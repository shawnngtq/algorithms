"""
https://leetcode.com/problems/maximum-subarray/
https://dev.to/13point5/maximum-subarray-3c5l
"""


def maximum_subarray_kadane_algo(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)


def maximum_subarray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximm subarray Kadane algorithm")
print(maximum_subarray_kadane_algo(nums))
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximm subarray")
print(maximum_subarray(nums))

nums = [1]
print("Maximm subarray Kadane algorithm")
print(maximum_subarray_kadane_algo(nums))
nums = [1]
print("Maximm subarray")
print(maximum_subarray(nums))

nums = [0]
print("Maximm subarray Kadane algorithm")
print(maximum_subarray_kadane_algo(nums))
nums = [0]
print("Maximm subarray")
print(maximum_subarray(nums))

nums = [-1]
print("Maximm subarray Kadane algorithm")
print(maximum_subarray_kadane_algo(nums))
nums = [-1]
print("Maximm subarray")
print(maximum_subarray(nums))

nums = [-2147483647]
print("Maximm subarray Kadane algorithm")
print(maximum_subarray_kadane_algo(nums))
nums = [-2147483647]
print("Maximm subarray")
print(maximum_subarray(nums))
