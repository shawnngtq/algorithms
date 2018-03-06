function reverseParentheses(s) {

  // method 1
  while (s != (s = s.replace(/\([^(]*?\)/, t => [...t].slice(1, -1).reverse().join(''))));
  return s;

  // // method 2
  // const sArray = s.split("")
  // const stack = []

  // while (sArray.indexOf('(') !== -1){
  //   for (var i = 0; i < sArray.length; i++){
  //     var curr = sArray[i]
  //     if (curr === '(') {
  //       stack.push(i)
  //       continue
  //     }
  //     if (curr === ')') {
  //       var start = stack.pop()
  //       var reversed = sArray.slice(start + 1, i).reverse()
  //       sArray.splice(start, i - start + 1, ...reversed)
  //       break
  //     }
  //   }
  // }
  // return sArray.join("")

  // // method 3: reverse search
  // while (s.indexOf(")",0)!=-1) {
  //   var c = s.indexOf(")", 0);
  //   var a = s.lastIndexOf('(', c);
  //   var b = s.slice(a + 1, c).split("").reverse().join("");
  //   var s = s.slice(0, a) +b + s.slice(c + 1); 
  // }
  // return s;

  // // method 4
  // while(s.indexOf('(') !== -1){
  //   s = s.replace(/\(([\w\s]*)\)/, (match, p) => {
  //     return p.split('').reverse().join('');
  //   })
  // }
  // return s;
};

var s = "a(bc)de";
console.log("acbde:", reverseParentheses(s));
var s = "a(bcdefghijkl(mno)p)q";
console.log("apmnolkjihgfedcbq:", reverseParentheses(s));
var s = "co(de(fight)s)";
console.log("cosfighted:", reverseParentheses(s));
var s = "Code(Cha(lle)nge)";
console.log("CodeegnlleahC:", reverseParentheses(s));
var s = "Where are the parentheses?";
console.log("Where are the parentheses?:", reverseParentheses(s));
var s = "abc(cba)ab(bac)c";
console.log("abcabcabcabc:", reverseParentheses(s));
var s = "The ((quick (brown) (fox) jumps over the lazy) dog)";
console.log("The god quick nworb xof jumps over the lazy:", reverseParentheses(s));
