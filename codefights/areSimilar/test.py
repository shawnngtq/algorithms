def areSimilar(a, b):

  # Method 1
  if a == b:
    return True

  temp = []
  for i in range(len(a)):
    if (a[i] != b[i]):
      temp.append(a[i])
      temp.append(b[i])
    if (len(temp) > 4):
      return False

  temp.sort()
  result = set(temp)
  return len(result) < 3

  # # Method 2
  # return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2

  # # Method 3
  # r = []
  # for i in range(len(A)):
  #   if A[i] != B[i]:
  #     r.append([A[i],B[i]])
        
  # if len(r) == 0 or len(r) == 2 and r[0]==r[1][::-1]:
  #   return True
  # return False


a = [1, 2, 3]
b = [1, 2, 3]
print(areSimilar(a,b))
a = [1, 2, 3]
b = [2, 1, 3]
print(areSimilar(a,b))
a = [1, 2, 2]
b = [2, 1, 1]
print(areSimilar(a,b))
a = [1, 1, 4]
b = [1, 2, 3]
print(areSimilar(a,b))
a = [1, 2, 3]
b = [1, 10, 2]
print(areSimilar(a,b))
a = [2, 3, 1]
b = [1, 3, 2]
print(areSimilar(a,b))
a = [2, 3, 9]
b = [10, 3, 2]
print(areSimilar(a,b))
a = [4, 6, 3]
b = [3, 4, 6]
print(areSimilar(a,b))
a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
print(areSimilar(a,b))
a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
print(areSimilar(a,b))