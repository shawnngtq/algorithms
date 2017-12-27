def palindromeRearranging(inputString):

  # Method 1
  # make a dictionary
  temp = {}
  for x in inputString:
    if x not in temp:
      temp[x] = 1
    else:
      temp[x] += 1

  length = len(inputString)
  if length % 2 == 0:
    return all(value % 2 == 0 for value in temp.values())
  else:
    odd = [v for v in temp.values() if v%2 == 1]
    if len(odd) == 1:
      return True
    else:
      return False

  # # Method 2
  # return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1


inputString = "aabb"
print(palindromeRearranging(inputString))
inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
print(palindromeRearranging(inputString))
inputString = "abbcabb"
print(palindromeRearranging(inputString))
inputString = "zyyzzzzz"
print(palindromeRearranging(inputString))
inputString = "z"
print(palindromeRearranging(inputString))
inputString = "zaa"
print(palindromeRearranging(inputString))
inputString = "abca"
print(palindromeRearranging(inputString))