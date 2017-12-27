function pivotedBinarySearch(arr, n, key) {
  var pivot = findPivot(arr, 0, n-1);

  if(pivot == -1) {
    return binarySearch(arr, 0, n-1, key);
  };

  if(key == arr[pivot]) {
    return pivot;
  };

  if(key >= arr[0]) {
    return binarySearch(arr, 0, pivot-1, key);
  };

  return binarySearch(arr, pivot+1, n-1, key);
};

function findPivot(arr, low, high) {
  if(low > high) {
    return -1;
  };
  if(low == high) {
    return low;
  };

  var mid = Math.floor((low+high)/2);
  if(mid < high && arr[mid] > arr[mid+1]) {
    return mid;
  };
  if(low < mid && arr[mid] < arr[mid-1]) {
    return mid-1;
  }
  if(arr[low] >= arr[mid]) {
    return findPivot(arr, low, mid-1);
  };
  return findPivot(arr, mid+1, high);
};

function binarySearch(arr, left, right, key) {
  if(left > right) {
    return -1;
  };

  var mid = Math.floor((left+right)/2);
  if(key == arr[mid]) {
    return mid;
  };
  if(key > arr[mid]) {
    return binarySearch(arr, mid+1, right, key);
  };

  return binarySearch(arr, left, mid-1, key);
};

var arr = [5, 6, 7, 8, 9, 10, 1, 2, 3];
console.log('Index of the element is:', pivotedBinarySearch(arr, arr.length, 3));





function search(arr, left, right, key) {
  if(left > right) {
    return -1;
  };

  var mid = Math.floor((left+right)/2);
  if(key == arr[mid]) {
    return mid;
  }

  if(arr[left] <= arr[mid]) {
    if(key >= arr[left] && key <= arr[mid]) {
      return search(arr, left, mid-1, key);
    };
    return search(arr, mid+1, right, key);
  };

  if(key >= arr[mid] && key <= arr[right]) {
    return search(arr, mid+1, right, key);
  };

  return search(arr, left, mid-1, key);
};

var arr = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3];
console.log('Index of the element is:', search(arr, 0, arr.length-1, 6));
