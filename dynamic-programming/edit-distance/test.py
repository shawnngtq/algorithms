# Naive recursive, O(3^m)
def editDistance(str1, str2, m, n):

  # C1: str1 is empty, insert all str2's characters to str1
  if(m == 0):
    return n

  # C2: str2 is empty, remove all str1's characters
  if(n == 0):
    return m

  # C3: if last char of both strings are same
  # Ignore the last char and get count for remaining char
  if(str1[m-1] == str2[n-1]):
    return editDistance(str1, str2, m-1, n-1)

  # C4: if last char of both strings are not same
  # recursively compute minimum cost for all three operations 
  # and take minimum of three values.
  minDistance = min(
    editDistance(str1, str2, m, n-1),  #Insert
    editDistance(str1, str2, m-1, n),  #Remove
    editDistance(str1, str2, m-1, n-1) #Replace
  )

  return 1 + minDistance

str1 = 'sunday'
str2 = 'saturday'
print(editDistance(str1, str2, len(str1), len(str2)))





# Tabulation, O(mn)
def editDistanceDP(str1, str2, m, n):
  table = [ [0]*(n+1) for i in range(m+1) ]

  for i in range(m+1):
    for j in range(n+1):
      # C1
      if(i == 0):
        table[i][j] = j
      # C2
      elif(j == 0):
        table[i][j] = i
      # C3
      elif(str1[i-1] == str2[j-1]):
        table[i][j] = table[i-1][j-1]
      # C4
      else:
        minDistance = min(
          table[i][j-1],  #Insert
          table[i-1][j],  #Remove
          table[i-1][j-1] #Replace
        )
        table[i][j] = 1 + minDistance

  return table[m][n]

str1 = 'geek'
str2 = 'gesek'
print(editDistanceDP(str1, str2, len(str1), len(str2)))

str1 = 'cat'
str2 = 'cut'
print(editDistanceDP(str1, str2, len(str1), len(str2)))

str1 = 'sunday'
str2 = 'saturday'
print(editDistanceDP(str1, str2, len(str1), len(str2)))