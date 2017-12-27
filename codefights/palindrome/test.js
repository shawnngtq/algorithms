function checkPalindrome(inputString) {
  // method 1
  var rev = inputString.split("").reverse().join("");
  return inputString == rev;

  // method 2
  // return [...inputString].reverse().join('') === inputString

  // method 3
  // var arr = inputString.split("");
  // var i = 0, len = arr.length;
  // for(i; i < len/2; i++) {
  // 	if(arr[i] != arr[len-i-1]) {
  // 		return false;
  // 	}
  // };
  // return true;
};

var inputString = "aabaa";
checkPalindrome(inputString);
var inputString = "abac";
checkPalindrome(inputString);
var inputString = "a";
checkPalindrome(inputString);
var inputString = "az";
checkPalindrome(inputString);
var inputString = "abacaba";
checkPalindrome(inputString);
var inputString = "z";
checkPalindrome(inputString);
var inputString = "aaabaaaa";
checkPalindrome(inputString);
var inputString = "zzzazzazz";
checkPalindrome(inputString);
var inputString = "hlbeeykoqqqqokyeeblh";
checkPalindrome(inputString);
var inputString = "hlbeeykoqqqokyeeblh";
checkPalindrome(inputString);
