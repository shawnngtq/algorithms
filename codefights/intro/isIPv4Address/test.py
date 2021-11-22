def isIPv4Address(inputString):

    # Method 1
    if len(inputString.split(".")) != 4:
        return False

    for x in inputString.split("."):
        if not x or not x.isnumeric() or (x.isnumeric() and int(x) > 255):
            return False
    return True

    # # Method 2
    # # Same as method 1, but with Python functions
    # p = s.split('.')
    # return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

    # # Method 3
    # import ipaddress
    # try:
    #   ipaddress.ip_address(inputString)
    # except:
    #   return False
    # return True

    # # Method 4
    # # Using regex
    # if re.match('\d+\.\d+\.\d+\.\d+$', inputString):
    #   for i in inputString.split('.'):
    #     if not 0<=int(i)<256:
    #       return False
    #   return True
    # return False


inputString = "172.16.254.1"
print(isIPv4Address(inputString))
inputString = "172.316.254.1"
print(isIPv4Address(inputString))
inputString = ".254.255.0"
print(isIPv4Address(inputString))
inputString = "1.1.1.1a"
print(isIPv4Address(inputString))
inputString = "0.254.255.0"
print(isIPv4Address(inputString))
inputString = "0..1.0"
print(isIPv4Address(inputString))
inputString = "1.1.1.1.1"
print(isIPv4Address(inputString))
inputString = "1.256.1.1"
print(isIPv4Address(inputString))
inputString = "a0.1.1.1"
print(isIPv4Address(inputString))
inputString = "0.1.1.256"
print(isIPv4Address(inputString))
inputString = "7283728"
print(isIPv4Address(inputString))
