def variableName(name):
  if name[0].isnumeric():
    return False
  for i in name:
    if not(i.isalpha() or i.isnumeric() or i == '_'):
      return False
  return True


def variableName(name):
  return name.isidentifier()


# test 1
name = "var_1__Int"
print(variableName(name))

# test 2
name = "qq-q"
print(variableName(name))

# test 3
name = "2w2"
print(variableName(name))

# test 4
name = " variable"
print(variableName(name))

# test 5
name = "va[riable0"
print(variableName(name))

# test 6
name = "variable0"
print(variableName(name))

# test 7
name = "a"
print(variableName(name))
