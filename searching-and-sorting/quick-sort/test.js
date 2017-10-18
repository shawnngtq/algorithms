function partition(arr, low, high) {
  var i = low-1;
  var pivot = arr[high];

  for(var j=low; j < high; j++) {
    if(arr[j] <= pivot) {
      i++;
      // swapping elements
      var temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    };
  };

  var temp = arr[i+1];
  arr[i+1] = arr[high];
  arr[high] = temp;
  return i+1
};

function quickSort(arr, low, high) {
  if(low < high) {
    var pi = partition(arr, low, high);

    quickSort(arr, low, pi-1);
    quickSort(arr, pi+1, high);
  };
};


var arr = [10, 7, 8, 9, 1, 5];
var n = arr.length
quickSort(arr, 0, n-1);
