# O(n*n)
def insertionSort(arr)
  n = arr.length
  for i in (1..n-1)
    key = arr[i]
    j = i-1
    while(j >= 0 && key < arr[j])
      arr[j+1] = arr[j]
      j -= 1
    end
    arr[j+1] = key
  end

  return arr
end

arr = [12, 11, 13, 5, 6]
p insertionSort(arr)





# O(n^2)
def binarySearch(arr, left, right, x)
  if(right <= left)
    return (x > arr[left]) ? (left+1) : left
  end

  mid = ((left+right)/2).to_i
  if(x == arr[mid])
    return mid+1
  end

  if(x > arr[mid])
    return binarySearch(arr, mid+1, right, x)
  end

  return binarySearch(arr, left, mid-1, x)
end

def binaryInsertionSort(arr)
  n = arr.length
  for i in (1..n-1)
    j = i-1
    key = arr[i]
    location = binarySearch(arr, 0, j, key)
    while(j >= location)
      arr[j+1] = arr[j]
      j -= 1
      arr[j+1] = key
    end
  end
  return arr
end

arr = [12, 11, 13, 5, 6]
p binaryInsertionSort(arr)