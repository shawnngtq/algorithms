def alphabeticShift(inputString):
  alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
  result = ''
  for i in inputString:
    result += alpha[(alpha.index(i)+1) % 26]
  return result


def alphabeticShift(inputString):
  return "".join(chr((ord(i)-96)%26+97) for i in inputString)


# test 1
inputString = "crazy"
print(alphabeticShift(inputString))
# expect "dsbaz"


# test 2
inputString = "z"
print(alphabeticShift(inputString))
# expect "a"