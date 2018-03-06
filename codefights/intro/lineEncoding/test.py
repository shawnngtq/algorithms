def lineEncoding(s):
    s=[i+j for i,j in re.findall(r"(\w)(\1*)",s)]
    ans=""
    for i in s:
        if len(i)==1:
            ans+=i
        else:
            ans+=str(len(i))+i[0]
    return ans


def lineEncoding(s):
    r = [m.group() for m in re.compile(r"(.)(\1*)").finditer(s)]
    s = ''
    for i in r:
        if len(i)==1:
            s+=i
        else:
            s+=str(len(i))+i[0]
    return s


def lineEncoding(s):
    
    def addMethod(result,k,v):
    	result += str(v) + k if v > 1 else v
        return result
            
    curr, count, result = s[0], 1, ''
    for i in s[1:]:
        if i == curr:
            count += 1
        else:
            result = addMethod(result, curr, count)
            curr, count = temp, 1

    result = addMethod(result, temp, count)
    return result


# test
s = "aabbbc"
print(lineEncoding(s))

# test
s = "abbcabb"
print(lineEncoding(s))

# test
s = "abcd"
print(lineEncoding(s))
