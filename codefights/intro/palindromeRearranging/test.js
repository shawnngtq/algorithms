function palindromeRearranging(s) {

  // method 1
  // author: myjinxin2015
  // get a sorted array
  var ss=s.split("").sort(), r=0;

  // if there is even number of element, r will not increase
  // else increase
  while(ss.length){
    var t=ss.shift();
    if(t===ss[0]) {ss.shift()}
    else r++;
  };
  return r<2;

  // // method 2
  // // author: jraghon
  // //histogram the characters
  // m = []
  // for(c of s)
  //   m[c] = -~m[c]
  // //count the unmatched characters
  // u = 0
  // for(x in m)
  //   u += m[x]%2
      
  // //confirm that the number of unmatched characters
  // //is the same as the oddness of the string
  // return u == s.length%2

};

var inputString = "aabb";
console.log(palindromeRearranging(inputString));
var inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc";
console.log(palindromeRearranging(inputString));
var inputString = "abbcabb";
console.log(palindromeRearranging(inputString));
var inputString = "zyyzzzzz";
console.log(palindromeRearranging(inputString));
var inputString = "z";
console.log(palindromeRearranging(inputString));
var inputString = "zaa";
console.log(palindromeRearranging(inputString));
var inputString = "abca";
console.log(palindromeRearranging(inputString));