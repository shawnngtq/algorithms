# Given two integers x and n, write a function to compute x^n. We may assume that x and n are small and overflow doesn’t happen

# Recursive method
# Time Complexity: O(n)
# Space Complexity: O(1)
# Algorithmic Paradigm: Divide and conquer
# Function to calculate x raised to the power y
def power(x, y):
  if(y == 0):
    return 1
  elif(y % 2 == 0):
    return power(x, int(y/2)) * power(x, int(y/2))
  else:
    return x * power(x, int(y/2)) * power(x, int(y/2))

x,y = 2,5
print('2**5=', power(2,5))


# Time Complexity: O(log(n))
def power(x, y):
  if(y == 0):
    return 1
  temp = power(x, int(y/2))
  if(y % 2 == 0):
    return temp*temp
  else:
    return x*temp*temp

x,y = 2,5
print('2**5=', power(2,5))





# Iterative method
# Time Complexity: O(log(n))
def power(x, y):
  res = 1
  while(y > 0):
    if(y % 2 == 1):
      res *= x

    y = int(y/2)
    x *= x
  return res

x,y = 2,5
print('2**5=', power(2,5))
