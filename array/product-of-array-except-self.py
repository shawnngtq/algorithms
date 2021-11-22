"""
https://leetcode.com/problems/product-of-array-except-self/
"""


def product_of_rest(nums):
    import math

    output = []
    for i in range(len(nums)):
        L, R = math.prod(nums[:i]), math.prod(nums[i + 1 :])
        output.append(L * R)
    return output


nums = [1, 2, 3, 4]
print("Product of rest")
print(product_of_rest(nums))
