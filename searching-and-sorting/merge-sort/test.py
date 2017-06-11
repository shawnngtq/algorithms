# O(n log n)
# Merges 2 subarrays of array
# 1st subarray: array[1..m]
# 2nd subarray: array[m+1..r]
'''
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
'''
def merge(arr, l, m, r):
  n1 = m-l+1
  n2 = r-m

  # create temp arrays
  L = [0]*(n1)
  R = [0]*(n2)

  # Copy data to temp arrays L[] and R[]
  for i in range(n1):
    L[i] = arr[l+i]

  for j in range(n2):
    R[j] = arr[m+1+j]

  # Merge the temp arrays back into arr[l..r]
  i = 0  # Initial index of 1st subarray
  j = 0  # Initial index of 2nd subarray
  k = l  # Initial index of merged subarray

  while(i < n1 and j < n2):
    # when L value is smaller than R value
    # update array value with L value
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  # Copy the remaining elements of L[], if there
  # are any
  while(i < n1):
    arr[k] = L[i]
    i += 1
    k += 1

  # Copy the remaining elements of R[], if there
  # are any
  while(j < n2):
    arr[k] = R[j]
    j += 1
    k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,l,r):
  if(l<r):

    # Same as (l+r)/2, but avoids overflow for
    # large l and h
    m = int((l+(r-1))/2)

    # Sort first and second halves
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)

arr = [12, 11, 13, 5, 6, 7]
print('Given array:', arr)
mergeSort(arr, 0, len(arr)-1)
print('Sorted array:', arr)