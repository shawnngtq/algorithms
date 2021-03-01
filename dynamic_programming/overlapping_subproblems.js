// MEMOIZATION
// Method 1, pre-defined lookup table
function fibonacci(n, lookup) {
  if(n < 2) {
    lookup[n] = n;
  };

  if(n >= lookup.length) {
    lookup[n] = fibonacci(n-1, lookup) + fibonacci(n-2, lookup);
  };

  return lookup[n];
};

fibonacci(34, []);


// Method 2, user don't need to specifiy lookup
function fibonacci(n, lookup=[]) {

  if(n < 2) {
    lookup[n] = n;
  };

  if(n >= lookup.length) {
    lookup[n] = fibonacci(n-1, lookup) + fibonacci(n-2, lookup);
  };

  return lookup[n];
};

fibonacci(34);


// Method 3, don't build lookup table from empty array
function fibonacci(n, lookup=[0,1]) {
  if(n >= lookup.length) {
    lookup[n] = fibonacci(n-1, lookup) + fibonacci(n-2, lookup);
  };

  return lookup[n];
}

fibonacci(34);





// TABULATION
function fibonacci(n) {
  var lookup = [0,1];

  var i = 2;
  for(i; i < n+1; i++) {
    lookup[i] = lookup[i-1] + lookup[i-2];
  };

  return lookup[n];
};

fibonacci(34);