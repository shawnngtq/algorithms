def firstDigit(inputString):
  return re.findall('\d', inputString)[0]


def firstDigit(inputString):
  result = re.search('\d', inputString)
  if result != None:
    return result.group()


def firstDigit(inputString):
  for i in inputString:
    if i.isdigit():
      return i


# test
inputString = "var_1__Int"
print(firstDigit(inputString))

# test
inputString = "q2q-q"
print(firstDigit(inputString))

# test
inputString = "0ss"
print(firstDigit(inputString))
