def isMAC48Address(inputString):
    for i in range(len(inputString)):
        if i % 3 == 2:
            if inputString[i] != "-":
                return False
        else:
            if not ("0" <= inputString[i] <= "9" or "A" <= inputString[i] <= "F"):
                return False
    return len(inputString) == 17


def isMAC48Address(s):
    return bool(re.match(("^" + "[\dA-F]{2}-" * 6)[:-1] + "$", s))


def isMAC48Address(inputString):
    d = "[0-9A-F]"
    m = re.match(
        "{}{}-{}{}-{}{}-{}{}-{}{}-{}{}$".format(d, d, d, d, d, d, d, d, d, d, d, d),
        inputString,
    )
    if m:
        return True
    return False


# test
inputString = "00-1B-63-84-45-E6"
print(isMAC48Address(inputString))

# test
inputString = "Z1-1B-63-84-45-E6"
print(isMAC48Address(inputString))

# test
inputString = "not a MAC-48 address"
print(isMAC48Address(inputString))

# test
inputString = "FF-FF-FF-FF-FF-FF"
print(isMAC48Address(inputString))

# test
inputString = "00-00-00-00-00-00"
print(isMAC48Address(inputString))

# test
inputString = "G0-00-00-00-00-00"
print(isMAC48Address(inputString))

# test
inputString = "02-03-04-05-06-07-"
print(isMAC48Address(inputString))

# test
inputString = "12-34-56-78-9A-BC"
print(isMAC48Address(inputString))

# test
inputString = "FF-FF-AB-CD-EA-BC"
print(isMAC48Address(inputString))

# test
inputString = "12-34-56-78-9A-BG"
print(isMAC48Address(inputString))
