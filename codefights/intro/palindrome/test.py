def checkPalindrome(inputString):
    # method 1
    return inputString == inputString[::-1]


inputString = "aabaa"
print(checkPalindrome(inputString))
inputString = "abac"
print(checkPalindrome(inputString))
inputString = "a"
print(checkPalindrome(inputString))
inputString = "az"
print(checkPalindrome(inputString))
inputString = "abacaba"
print(checkPalindrome(inputString))
inputString = "z"
print(checkPalindrome(inputString))
inputString = "aaabaaaa"
print(checkPalindrome(inputString))
inputString = "zzzazzazz"
print(checkPalindrome(inputString))
inputString = "hlbeeykoqqqqokyeeblh"
print(checkPalindrome(inputString))
inputString = "hlbeeykoqqqokyeeblh"
print(checkPalindrome(inputString))
