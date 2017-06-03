# http://www.geeksforgeeks.org/dynamic-programming-set-1/

# MEMOIZATION
def fibonacci(n, lookup):
  # Base case
  if n < 2:
    lookup[n] = n

  # If the value is not calculated previously 
  # then calculate it
  if lookup[n] is None:
    lookup[n] = fibonacci(n-1, lookup) + fibonacci(n-2, lookup)

  return lookup[n]

def main():
  n = 34
  # lookup table with maximum n = 100
  lookup = [None]*(101)
  print('Fibonacci Number is ', fibonacci(n, lookup))

print('Memoization: top down method')
main()




# TABULATION
def fibonacci2(n):
  # Declare size of array
  f = [0]*(n+1)

  # Base declaration
  f[1] = 1

  for i in range(2, n+1):
    f[i] = f[i-1] + f[i-2]
  return f[n]

def main2():
  n = 9
  print('Fibonacci number is ', fibonacci2(n))

print('Tabulation: bottom up method')
main2()