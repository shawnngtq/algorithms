function isIPv4Address(s) {
  
  // Method 1
  var  r=s.split(".")
  return r.length===4&&r.every(x=>x!=""&&!isNaN(x)&&x>=0&&x<256)

  // // Method 2
  // // Regex method
  // a = inputString.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
  // return Boolean(a && (a[1]|0) < 256 && (a[2]|0) < 256 && (a[3]|0) < 256 && (a[4]|0) < 256)

  // // Method 3
  // inputString = inputString.split(".")
  // if(inputString.length !== 4) return false
  // for(i in inputString){
  //   var z = parseInt(inputString[i])
  //   if(z > 255 || z < 0 || inputString[i] == "" || isNaN(inputString[i])) return false 
  // }
  // return true
};

var inputString = "172.16.254.1";
console.log(isIPv4Address(inputString));
var inputString = "172.316.254.1";
console.log(isIPv4Address(inputString));
var inputString = ".254.255.0";
console.log(isIPv4Address(inputString));
var inputString = "1.1.1.1a";
console.log(isIPv4Address(inputString));
var inputString = "0.254.255.0";
console.log(isIPv4Address(inputString));
var inputString = "0..1.0";
console.log(isIPv4Address(inputString));
var inputString = "1.1.1.1.1";
console.log(isIPv4Address(inputString));
var inputString = "1.256.1.1";
console.log(isIPv4Address(inputString));
var inputString = "a0.1.1.1";
console.log(isIPv4Address(inputString));
var inputString = "0.1.1.256";
console.log(isIPv4Address(inputString));
var inputString = "7283728";
console.log(isIPv4Address(inputString));
