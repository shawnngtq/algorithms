def buildPalindrome(st):
    for i in range(len(st)):
        s = st + st[i::-1]
        if s == s[::-1]:
            return s
    

def buildPalindrome(st):
    return re.sub(r'(\w+)\1', r'\1', st + st[::-1])


def buildPalindrome(st):
    i = 0
    while st[i:] != st[i:][::-1]:
        i += 1
        if i == len(st):
            break
    st += st[:i][::-1]
    return st


# test
st = "abcdc"
print(buildPalindrome(st))

# test
st = "ababab"
print(buildPalindrome(st))

# test
st = "abba"
print(buildPalindrome(st))

# test
st = "abaa"
print(buildPalindrome(st))
