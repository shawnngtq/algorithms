# Given three numbers x, y and p, compute (x^y) % p

# Refer to power.py
# Time Complexity: O(log(n))
def modExp(x, y, p):
  res = 1
  x %= p

  while(y > 0):
    if(y % 2 == 1):
      res = (res*x) % p

    y = int(y/2)
    x = (x*x) % p

  return res

x,y,p = 2,5,13
print('2**5 % 13=', modExp(x,y,p))