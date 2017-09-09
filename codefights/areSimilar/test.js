function areSimilar(A, B) {

  // Method 1
  var r = 0;
  for(i in A){
    if(B.indexOf(A[i]) == -1){
      return false
    }
    if(B[i] !== A[i]){
      r++
    }
  }
  return r%2==0 && r < 3

  // Method 2
  // for(var r=[],i=0;i<A.length;i++) if(A[i]!=B[i]) r.push(A[i],B[i])
  // return r.length<5&&new Set(r).size<3
}
