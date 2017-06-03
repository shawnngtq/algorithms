function LIS(array) {
  var n = array.length;

  var lis = Array(n).fill(1);

  var i = 1;
  for(i; i < n; i++) {
    // declaring j inside loop function is different from
    // declaring it outside
    for(var j = 0; j < i; j++) {
      if(array[i] > array[j] && lis[i] < lis[j] + 1) {
        lis[i] = lis[j] + 1;
      };
    };
  };

  var maximum = Math.max.apply(null,lis) || 0;

  return maximum;
};

var array = [10, 22, 9, 33, 21, 50, 41, 60];
LIS(array);

var array2 = [3, 10, 2, 1, 20];
LIS(array2);

var array3 = [3, 2];
LIS(array3);

var array4 = [50, 3, 10, 7, 40, 80];
LIS(array4);