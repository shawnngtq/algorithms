def mergeSort(arr, l, r)
  if(l<r)
    m = ((l+(r-1))/2).floor

    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)
  end
end

def merge(arr, l, m, r)
  n1 = m-l+1
  n2 = r-m

  leftSubArr = [0]*n1
  rightSubArr = [0]*n2

  for i in (0..n1-1)
    leftSubArr[i] = arr[l+i]
  end

  for j in (0..n2-1)
    rightSubArr[j] = arr[m+1+j]
  end

  i = 0
  j = 0
  k = l

  while(i < n1 && j < n2)
    if(leftSubArr[i] <= rightSubArr[j])
      arr[k] = leftSubArr[i]
      i += 1
    else
      arr[k] = rightSubArr[j]
      j += 1
    end
    k += 1
  end

  while(i < n1)
    arr[k] = leftSubArr[i]
    i += 1
    k += 1
  end

  while(j < n2)
    arr[k] = rightSubArr[j]
    j += 1
    k += 1
  end
end

arr = [12, 11, 13, 5, 6, 7]
p 'Given array:' 
p arr
mergeSort(arr, 0, arr.length-1)
p 'Sorted array:'
p arr