def longestWord(text):
    return max(re.split('[^a-zA-Z]', text), key=len)


# unit test
# Expected Output: "steady"
text = "Ready, steady, go!"
print(longestWord(text))

# unit test
# Expected Output: "steady"
text = "Ready[[[, steady, go!"
print(longestWord(text))

# unit test
# Expected Output: "ABCd"
text = "ABCd"
print(longestWord(text))