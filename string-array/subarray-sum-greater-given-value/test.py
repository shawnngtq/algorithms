# http://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
# O(n)
# Returns length of smallest subarray with sum greater than x.
# If there is no subarray with given sum, then returns n+1
def smallestSubWithSum(arr, n, x):

  # Initialize current sum and minimum length
  curr_sum, min_len = 0, n+1
  # Initialize starting and ending indexes
  start, end = 0, 0

  while(end < n):
    # Keep adding array elements while current sum
    # is smaller than x
    while(curr_sum <= x and end < n):

      # Ignore subarrays with negative sum if
      # x is positive.
      if(curr_sum <= 0 and x > 0):
        start = end
        curr_sum = 0

      curr_sum += arr[end]
      end += 1

    # If current sum becomes greater than x.
    while(curr_sum > x and start < n):
      # Update minimum length if needed
      if(end - start < min_len):
        min_len = end-start

      # remove starting elements
      curr_sum -= arr[start]
      start += 1

  if(min_len > n):
    print('Not possible')
  else:
    print('Possible')
  return min_len

 

arr1 = [1, 4, 45, 6, 0, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x)
print('Minimum length:', res1)

arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubWithSum(arr2, n2, x)
print('Minimum length:', res2)

arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubWithSum(arr3, n3, x)
print('Minimum length:', res3)

arr4 = [1, 10, 3, 40, 18]
n4 = len(arr4)
x = 50
res4 = smallestSubWithSum(arr4, n4, x)
print('Minimum length:', res4)

arr5 = [1, 2, 4]
n5 = len(arr5)
x = 8
res5 = smallestSubWithSum(arr5, n5, x)
print('Minimum length:', res5)

arr6 = [-8, 1, 4, 2, -6]
n6 = len(arr6)
x = 6
res6 = smallestSubWithSum(arr6, n6, x)
print('Minimum length:', res6)