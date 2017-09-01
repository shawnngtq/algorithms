function avoidObstacles(arr) {

  // Method 1
  for(var n=1;;n++) {
    if(arr.every(x=>x%n)) {
      return n;
    }
  };

  // // Method 2
  // var jump = 2;
  // while (inputArray.some((obstacle) => obstacle % jump == 0)) {
  //   jump++;
  // }
  // return jump;
};

var inputArray = [5, 3, 6, 7, 9];
console.log(avoidObstacles(inputArray));
var inputArray = [2, 3];
console.log(avoidObstacles(inputArray));
var inputArray = [1, 4, 10, 6, 2];
console.log(avoidObstacles(inputArray));
