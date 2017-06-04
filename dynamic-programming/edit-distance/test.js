// Naive recursive, O(3^m)
function editDistance(str1, str2, m, n) {
  // C1: str1 is empty, insert all str2's characters to str1
  if(m == 0) {
    return n;
  };

  // C2: str2 is empty, remove all str1's characters
  if(n == 0) {
    return m;
  };

  // C3: if last char of both strings are same
  // Ignore the last char and get count for remaining char
  if(str1[m-1] == str2[n-1]) {
    return editDistance(str1, str2, m-1, n-1);
  };

  // C4: if last char of both strings are not same
  // recursively compute minimum cost for all three operations 
  // and take minimum of three values.
  var minDistance = Math.min(
    editDistance(str1, str2, m, n-1),   //Insert
    editDistance(str1, str2, m-1, n),   //Remove
    editDistance(str1, str2, m-1, n-1)  //Replace
  );

  return 1 + minDistance;
};

var str1 = 'sunday';
var str2 = 'saturday';
console.log(editDistance(str1, str2, str1.length, str2.length));





// Tabulation, O(mn)
function editDistanceDP(str1, str2, m, n) {
  var table = Array(m+1).fill().map(a => Array(n+1).fill(0));

  for(var i = 0; i < m+1; i++) {
    for(var j = 0; j < n+1; j++) {
      // C1
      if(i == 0) {
        table[i][j] = j;
      }
      // C2
      else if(j == 0) {
        table[i][j] = i;
      }
      // C3
      else if(str1[i-1] == str2[j-1]) {
        table[i][j] = table[i-1][j-1];
      }
      // C4
      else {
        var minDistance = Math.min(
          table[i][j-1],
          table[i-1][j],
          table[i-1][j-1]
        );
        table[i][j] = 1 + minDistance;
      };
    };
  };

  return table[m][n];
};

var str1 = 'geek';
var str2 = 'gesek';
console.log(editDistanceDP(str1, str2, str1.length, str2.length));

var str1 = 'cat';
var str2 = 'cut';
console.log(editDistanceDP(str1, str2, str1.length, str2.length));

var str1 = 'sunday';
var str2 = 'saturday';
console.log(editDistanceDP(str1, str2, str1.length, str2.length));