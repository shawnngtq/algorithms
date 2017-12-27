# Recursive search, O(log n)
def binarySearch(array, left, right, x)
  if(right >= left)
    mid = left + (right-left)/2

    if(x == array[mid])
      return mid
    elsif(x < array[mid])
      return binarySearch(array, left, mid-1, x)
    else
      return binarySearch(array, mid+1, right, x)
    end

  else
    return -1
  end
end

array = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(array, 0, array.size-1, x)

puts (result == -1) ? 'Element is not present in array' : "Element is present at index %d" %result





# Iterative search, O(log n)
def binarySearch(array, left, right, x)
  while right > left
    mid = left + (right-left)/2

    if(x == array[mid])
      return mid
    elsif(x < array[mid])
      right = mid-1
    else
      left = mid+1
    end
  end
  return -1
end

array = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(array, 0, array.size-1, x)

puts (result == -1) ? 'Element is not present in array' : "Element is present at index %d" %result