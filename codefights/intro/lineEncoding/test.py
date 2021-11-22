import re


def lineEncoding(s):
    s = [i + j for i, j in re.findall(r"(\w)(\1*)", s)]
    ans = ""
    for i in s:
        if len(i) == 1:
            ans += i
        else:
            ans += str(len(i)) + i[0]
    return ans


def lineEncoding(s):
    r = [m.group() for m in re.compile(r"(.)(\1*)").finditer(s)]
    s = ""
    for i in r:
        if len(i) == 1:
            s += i
        else:
            s += str(len(i)) + i[0]
    return s


# test
s = "aabbbc"
print(lineEncoding(s))

# test
s = "abbcabb"
print(lineEncoding(s))

# test
s = "abcd"
print(lineEncoding(s))
