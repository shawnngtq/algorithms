// Recursive method, O(2^n)
// Returns minimum value of the difference of 2 subsets
function findMinDiff(array, n) {
  // Compute total sum of elements
  var totalSum = 0;
  for(var i = 0; i < n; i++) {
    totalSum += array[i];
  };

  // Compute result using recursive function
  return findMinSum(array, n, 0, totalSum);
};

// Function to find the minimum sum
function findMinSum(array, i, subset1Sum, totalSum) {

  // When we reached the last element
  // return the absolute value of difference between
  // subset 1 and subset 2 sum
  var subset2Sum = totalSum - subset1Sum;
  if(i == 0) {
    return Math.abs(subset2Sum - subset1Sum);
  };

  // For every item array[i], 2 choices
  // 1) Include in subset 1
  // 2) Include in subset 2
  // return the minimum of 2 choices
  var minimum = Math.min(
    findMinSum(array, i-1, subset1Sum + array[i-1], totalSum),
    findMinSum(array, i-1, subset1Sum, totalSum)
  );

  return minimum;
};

var array = [3, 1, 4, 2, 2, 1];
var n = array.length;
console.log("The minimum difference between 2 sets is:", findMinDiff(array, n));





// Tabulation, O(n^sum)
function findMinDiffDP(array, n) {
  var totalSum = 0;
  for(var i = 0; i < n; i++) {
    totalSum += array[i];
  };

  var table = Array(totalSum+1).fill().map(a => Array(n+1));

  // Initialize 1st col as true
  for(var i = 0; i < n+1; i++) {
    table[i][0] = true;
  };

  // Initialize 1st row, except table[0][0] as false
  for(var j = 1; j < totalSum+1; j++) {
    table[0][j] = false;
  };

  // Tabulation
  for(var i = 1; i < n+1; i++) {
    for(var j = 1; j < totalSum+1; j++) {
      table[i][j] = table[i-1][j];
      if(array[i-1] <= j) {
        table[i][j] |= table[i-1][j-array[i-1]];
      };
    };
  };

  var diff;
  for(var j = Math.floor(totalSum/2); j > 0; j--) {
    if(table[n][j] == true) {
      diff = totalSum - (2*j);
      break;
    };
  };

  return diff;
};

var array = [3, 1, 4, 2, 2, 1];
var n = array.length;
console.log("The minimum difference between 2 sets is:", findMinDiffDP(array, n));

var array = [1, 6, 11, 5];
var n = array.length;
console.log("The minimum difference between 2 sets is:", findMinDiffDP(array, n));