def reverseParentheses(s):

    # method 1
    # find indexes of (
    start = [i for i, v in enumerate(s) if v == "("]
    # find indexes of )
    end = [i for i, v in enumerate(s) if v == ")"]
    while start and end:
        # take the last open
        startI = start.pop()
        # pick the smallest end that is greater than startI
        for i in end:
            if i > startI:
                iValue = i
                break
        endI = end.pop(end.index(iValue))
        origin = s[startI:endI]
        replacement = s[startI:endI][::-1]
        s = s.replace(origin, replacement)
    s = s.replace("(", "").replace(")", "")
    return s

    # method 2: recursive method
    # for i in range(len(s)):
    #   if s[i] == "(":
    #     start = i
    #   if s[i] == ")":
    #     end = i
    #     return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    # return s

    # method 3: reverse find
    # while ')' in s:
    #   j = s.index(')')
    #   i = s.rfind('(',0,j)
    #   s = s[:i]+s[j-1:i:-1]+s[j+1:]
    # return s

    # method 4: regex
    # while '(' in s:
    #   s=re.sub(r"\(([^()]+)\)",lambda x: x.group(1)[::-1],s)
    # return s


s = "a(bc)de"
print("acbde:", reverseParentheses(s))
s = "a(bcdefghijkl(mno)p)q"
print("apmnolkjihgfedcbq:", reverseParentheses(s))
s = "co(de(fight)s)"
print("cosfighted:", reverseParentheses(s))
s = "Code(Cha(lle)nge)"
print("CodeegnlleahC:", reverseParentheses(s))
s = "Where are the parentheses?"
print("Where are the parentheses?:", reverseParentheses(s))
s = "abc(cba)ab(bac)c"
print("abcabcabcabc:", reverseParentheses(s))
s = "The ((quick (brown) (fox) jumps over the lazy) dog)"
print("The god quick nworb xof jumps over the lazy:", reverseParentheses(s))
