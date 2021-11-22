def isBeautifulString(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]
    return r[::-1] == sorted(r)


def isBeautifulString(s):
    l = [[i, s.count(i)] for i in set(s)]
    l = sorted(l)
    for i in range(len(l) - 1):
        if l[i][0] != chr(97 + i) or l[i + 1][1] > l[i][1]:
            return False
    return True


def isBeautifulString(inputString):
    li = list(inputString)
    li.sort()

    result = []
    for i in range(97, ord(li[-1]) + 1):
        if chr(i) not in li:
            result.append((chr(i), 0))
        else:
            result.append((chr(i), li.count(chr(i))))

    print(result)
    for i in range(len(result) - 1):
        if result[i][1] == 0 or result[i + 1][1] > result[i][1]:
            return False
    return True


# test
inputString = "bbbaacdafe"
print(isBeautifulString(inputString))

# test
inputString = "aabbb"
print(isBeautifulString(inputString))

# test
inputString = "bbc"
print(isBeautifulString(inputString))

# test
inputString = "bbbaa"
print(isBeautifulString(inputString))

# test
inputString = "abcdefghijklmnopqrstuvwxyzz"
print(isBeautifulString(inputString))

# test
inputString = "abcdefghijklmnopqrstuvwxyz"
print(isBeautifulString(inputString))

# test
inputString = "abcdefghijklmnopqrstuvwxyzqwertuiopasdfghjklxcvbnm"
print(isBeautifulString(inputString))

# test
inputString = "fyudhrygiuhdfeis"
print(isBeautifulString(inputString))

# test
inputString = "zaa"
print(isBeautifulString(inputString))

# test
inputString = "zyy"
print(isBeautifulString(inputString))
