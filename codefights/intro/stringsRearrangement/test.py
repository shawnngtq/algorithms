import itertools


def stringsRearrangement(inputArray):
    def f(x, y):
        c = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1
        if c == 1:
            return True
        return False

    for k in itertools.permutations(inputArray, len(inputArray)):
        r = True
        for i in range(len(k) - 1):
            if not f(k[i], k[i + 1]):
                r = False
        if r:
            return True

    return False


from itertools import permutations


def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1


def stringsRearrangement(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False


# test
inputArray = ["aba", "bbb", "bab"]
print(stringsRearrangement(inputArray))

# test
inputArray = ["ab", "bb", "aa"]
print(stringsRearrangement(inputArray))

# test
inputArray = ["q", "q"]
print(stringsRearrangement(inputArray))

# test
inputArray = ["zzzzab", "zzzzbb", "zzzzaa"]
print(stringsRearrangement(inputArray))

# test
inputArray = ["ab", "ad", "ef", "eg"]
print(stringsRearrangement(inputArray))

# test
inputArray = ["abc", "bef", "bcc", "bec", "bbc", "bdc"]
print(stringsRearrangement(inputArray))

# test
inputArray = ["abc", "abx", "axx", "abc"]
print(stringsRearrangement(inputArray))

# test
inputArray = ["abc", "abx", "axx", "abx", "abc"]
print(stringsRearrangement(inputArray))

# test
inputArray = ["f", "g", "a", "h"]
print(stringsRearrangement(inputArray))
