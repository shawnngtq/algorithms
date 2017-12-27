# O(n^2)
def bubbleSort(arr)
  n = arr.length
  for i in (0..n-1)
    for j in (0..n-i-2)
      if(arr[j+1] && arr[j] > arr[j+1])
        arr[j], arr[j+1] = arr[j+1], arr[j]
      end
    end
  end

  # (0..n).each do |i|
  #   (0..n-i+1).each do |j|
  #     if(arr[j+1] && arr[j] > arr[j+1])
  #       arr[j], arr[j+1] = arr[j+1], arr[j]
  #     end
  #   end
  # end

  return arr
end

arr = [64, 34, 25, 12, 22, 11, 90]
p bubbleSort(arr)





# O(n*n) or O(n)
def bubbleSort(arr)
  n = arr.length

  for i in (0..n-2)
    swapped = false
    for j in (0..n-i-2)
      if(arr[j+1] && arr[j] > arr[j+1])
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = true
      end
    end
    if(swapped == false)
      break
    end
  end
  return arr
end

arr = [64, 34, 25, 12, 22, 11, 90]
p bubbleSort(arr)
