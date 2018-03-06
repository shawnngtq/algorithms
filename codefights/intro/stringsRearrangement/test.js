function stringsRearrangement(inputArray) {
  var bruteForce = function(depth, inputArray) {
    var swap = function(i, j) {
      tmp = inputArray[i];
      inputArray[i] = inputArray[j];
      inputArray[j] = tmp;
    };
    if (depth === inputArray.length) {
      var correct = true;
      for (var i = 0; i < inputArray.length - 1; i++) {
        var differences = 0;
        for (var j = 0; j < inputArray[i].length; j++) {
          if (inputArray[i][j] !== inputArray[i + 1][j]) {
            differences++;
          }
        }
        if (differences !== 1) {
          correct = false;
        }
      }
      if (correct) {
        return true;
      }
      return false;
    }
    for (var i = depth; i < inputArray.length; i++) {
      swap(depth, i);
      if (bruteForce(depth + 1, inputArray)) {
        return true;
      }
      swap(depth, i);
    }
    return false;
  };
  if (bruteForce(0, inputArray)) {
    return true;
  }
  return false;
};


// test
var inputArray = ["aba", "bbb", "bab"];
console.log(stringsRearrangement(inputArray));

// test
var inputArray = ["ab", "bb", "aa"];
console.log(stringsRearrangement(inputArray));

// test
var inputArray = ["q", "q"];
console.log(stringsRearrangement(inputArray));

// test
var inputArray = ["zzzzab", "zzzzbb", "zzzzaa"];
console.log(stringsRearrangement(inputArray));

// test
var inputArray = ["ab", "ad", "ef", "eg"];
console.log(stringsRearrangement(inputArray));

// test
var inputArray = ["abc", "bef", "bcc", "bec", "bbc;", "bdc"]
console.log(stringsRearrangement(inputArray));

// test
var inputArray = ["abc", "abx", "axx", "abc"];
console.log(stringsRearrangement(inputArray));

// test
var inputArray = ["abc", "abx", "axx", "abx", "abc;"]
console.log(stringsRearrangement(inputArray));

// test
var inputArray = ["f", "g", "a", "h"];
console.log(stringsRearrangement(inputArray));
