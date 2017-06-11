# O(log n)
'''
Input arr[] = {3, 4, 5, 1, 2}
Element to Search = 1
  1) Find out pivot point and divide the array in two
      sub-arrays. (pivot = 2) /*Index of 5*/
  2) Now call binary search for one of the two sub-arrays.
      (a) If element is greater than 0th element then
             search in left array
      (b) Else Search in right array
          (1 will go in else as 1 < 0th element(3))
  3) If element is found in selected sub-array then return index
     Else return -1.
'''
def pivotedBinarySearch(arr, n, key):
  pivot = findPivot(arr, 0, n-1)

  # if no pivot, it means array is not rotated
  if(pivot == -1):
    return binarySearch(arr, 0, n-1, key)

  # if pivot, 1st compare with pivot
  # then search 2 subarrays around pivot
  if(key == arr[pivot]):
    return pivot
  if(key >= arr[0]):
    return binarySearch(arr, 0, pivot-1, key)

  return binarySearch(arr, pivot+1, n-1, key)

def findPivot(arr, low, high):
  if(low > high):
    return -1
  if(low == high):
    return low

  mid = int((low+high)/2)
  if(mid < high and arr[mid] > arr[mid+1]):
    return mid
  if(low < mid and arr[mid] < arr[mid-1]):
    return mid-1
  if(arr[low] >= arr[mid]):
    return findPivot(arr, low, mid-1)

  return findPivot(arr, mid+1, high)

def binarySearch(arr, left, right, key):
  if(left > right):
    return -1

  mid = int((left+right)/2)
  if(key == arr[mid]):
    return mid
  if(key > arr[mid]):
    return binarySearch(arr, mid+1, right, key)

  return binarySearch(arr, left, mid-1, key)

arr = list(range(5,11)) + list(range(1,4))
print('Index of the element is:', pivotedBinarySearch(arr, len(arr), 3))





'''
1) Find middle point mid = (left + right)/2
2) If key is present at middle point, return mid.
3) Else If arr[left..mid] is sorted
    a) If key to be searched lies in range from arr[left]
       to arr[mid], recur for arr[left..mid].
    b) Else recur for arr[mid+1..right]
4) Else (arr[mid+1..right] must be sorted)
    a) If key to be searched lies in range from arr[mid+1]
       to arr[right], recur for arr[mid+1..right].
    b) Else recur for arr[left..mid]
'''
def search(arr, left, right, key):
  # if key not present
  if(left > right):
    return -1

  mid = int((left+right)/2)
  if(key == arr[mid]):
    return mid

  # If array[left..mid] is sorted
  if(arr[left] <= arr[mid]):
    # as subarray is sorted, we can check if key
    # lies in half or other half
    if(key >= arr[left] and key <= arr[mid]):
      return search(arr, left, mid-1, key)

    return search(arr, mid+1, right, key)

  # if array[left..mid] is not sorted
  # then array[mid..right] must be sorted
  if(key >= arr[mid] and key <= arr[right]):
    return search(arr, mid+1, right, key)

  return search(arr, left, mid-1, key)

arr = list(range(4,11)) + list(range(1,4))
print(search(arr, 0, len(arr)-1, 6))