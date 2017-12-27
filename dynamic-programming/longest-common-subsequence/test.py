# Recursive, O(2^n)
def LCS(X, Y, m, n):
  if(m == 0 or n == 0):
    return 0
  elif X[m-1] == Y[n-1]:
    return 1 + LCS(X, Y, m-1, n-1)
  else:
    return max(LCS(X, Y, m-1, n), LCS(X, Y, m, n-1))

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", LCS(X, Y, len(X), len(Y)))


# Overlapping Substructure, Tabulation, O(mn)
def LCS(X, Y):
  m = len(X)
  n = len(Y)

  L = [ [None]*(n+1) for i in range(m+1) ]

  # build L[m+1][n+1] bottom up
  # L[i][j] contains length of LCS of X[0..i-1]
  # and Y[0..j-1]
  for i in range(m+1):
    for j in range(n+1):
      if(i == 0 or j == 0):
        L[i][j] = 0
      elif(X[i-1] == Y[j-1]):
        L[i][j] = L[i-1][j-1] + 1
      else:
        L[i][j] = max(L[i-1][j], L[i][j-1])

  # L[m][n] contains LCS of X[0..m-1] & Y[0..n-1]
  return L[m][n]

X = "ABCDGH"
Y = "AEDFHR"
print("Length of LCS is ", LCS(X, Y))

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", LCS(X, Y))