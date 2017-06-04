// Overlapping substructure, Tabulation, O(mn)
function LCS(X, Y) {
  var m = X.length;
  var n = Y.length;

  var table = Array(n+1).fill().map(a => Array(m+1));

  for(var i = 0; i < m+1; i++) {
    for(var j = 0; j < n+1; j++) {
      if(i == 0 || j == 0) {
        table[i][j] = 0;
      }
      else if(X[i-1] == Y[j-1]) {
        table[i][j] = table[i-1][j-1] + 1;
      }
      else {
        table[i][j] = Math.max(table[i-1][j], table[i][j-1]);
      };
    };
  };

  return table[m][n];
};

var X = 'ABCDGH';
var Y = 'AEDFHR';
console.log('Length of LCS is: ', LCS(X, Y));

var X = 'AGGTAB';
var Y = 'GXTXAYB';
console.log('Length of LCS is: ', LCS(X, Y));