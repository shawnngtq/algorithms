# http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/

def LIS(array):
  n = len(array)

  # Declare the list (array) for LIS and initialize LIS
  # values for all indexes
  lis = [1]*n

  # Tabulation: bottom up method
  for i in range(1, n):
    for j in range(0, i):
      if(array[i] > array[j] and lis[i] < lis[j] + 1):
        lis[i] = lis[j] + 1

  # Make maximum = 0
  # Objective: get the maximum of all LIS
  maximum = 0

  # Pick the maximum of all LIS values
  for i in range(n):
    maximum = max(maximum, lis[i])

  return maximum


array = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is ", LIS(array))

array2 = [3, 10, 2, 1, 20]
print("Length of lis is ", LIS(array2))

array3 = [3, 2]
print("Length of lis is ", LIS(array3))

array4 = [50, 3, 10, 7, 40, 80]
print("Length of lis is ", LIS(array4))