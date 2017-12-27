function adjacentElementsProduct(inputArray) {
  // method 1
  var prod;
  var maxVal = -Infinity;
  var len = inputArray.length;
  for(var i = 1; i < len; i++) {
    prod = inputArray[i]*inputArray[i-1];
    maxVal = (prod > maxVal) ? prod : maxVal;
  };
  return maxVal;

  // method 2
  // var prod = inputArray[0] * inputArray[1]; 
  // for (var i = 1; i<inputArray.length - 1; i++) {
  //   prod = Math.max(prod, inputArray[i] * inputArray[i+1]);
  // }    
  // return prod

  // method 3
  // return Math.max(...arr.slice(1).map((x,i)=>[x*arr[i]]))
};

var inputArray = [3, 6, -2, -5, 7, 3];
adjacentElementsProduct(inputArray);
var inputArray = [-1, -2];
adjacentElementsProduct(inputArray);
var inputArray = [5, 1, 2, 3, 1, 4];
adjacentElementsProduct(inputArray);
var inputArray = [1, 2, 3, 0];
adjacentElementsProduct(inputArray);
var inputArray = [9, 5, 10, 2, 24, -1, -48];
adjacentElementsProduct(inputArray);
var inputArray = [5, 6, -4, 2, 3, 2, -23];
adjacentElementsProduct(inputArray);
var inputArray = [4, 1, 2, 3, 1, 5];
adjacentElementsProduct(inputArray);
var inputArray = [-23, 4, -3, 8, -12];
adjacentElementsProduct(inputArray);
var inputArray = [1, 0, 1, 0, 1000];
adjacentElementsProduct(inputArray);