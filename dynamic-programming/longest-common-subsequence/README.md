### Longest Common Subsequence

A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 

For example, "abc", "abg", "bdf", "aeg", ‘"acefg", .. etc are subsequences of "abcdefg". 

So a string of length n has `2^n` different possible subsequences

**Examples**:
```
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.
```

**Algorithm**:
1) If last characters of both sequences match (or `X[m-1] == Y[n-1]`) then
`L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])`

2) If last characters of both sequences do not match (or `X[m-1] != Y[n-1]`) then
`L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2])`

Link: http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/