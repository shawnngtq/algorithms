"""
https://leetcode.com/problems/maximum-product-subarray/
https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple
"""


def maximum_product_subarray(A):
    B = A[::-1]
    for i in range(1, len(A)):
        A[i] *= A[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(A + B)


nums = [2, 3, -2, 4]
print("Maximum product subarray")
print(maximum_product_subarray(nums))

nums = [-2, 0, -1]
print("Maximum product subarray")
print(maximum_product_subarray(nums))
