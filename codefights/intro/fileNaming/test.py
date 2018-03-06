# Method 1
def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names

# Method 2
def fileNaming(names):
    r = []
    d = {}
    for i in names:
        if i not in r:
            r.append(i)
            d[i] = 0
        else:
            d[i] = d.get(i,0) + 1
            while i+'({})'.format(d[i]) in r:
                d[i] = d.get(i,0) + 1
            r.append(i+'({})'.format(d[i]))
    return r

# Method 3
def fileNaming(names):
    output = [names[0]]
    for i in range(1,len(names)):
        if names[i] in names[0:i] or names[i] in output[0:i]:
            j = names[0:i].count(names[i])
            k = output[0:i].count(names[i])
            j = max(j,k)
            temp = names[i]+"("+str(j)+")"
            while temp in output[0:i]:
                j+=1
                temp = names[i]+"("+str(j)+")"
            output.append(temp)
        else:
            output.append(names[i])
    return output


# Unit test
names = ["doc",
 "doc",
 "image",
 "doc(1)",
 "doc"]
 print(fileNaming(names))
# Expected Output = ["doc",
#  "doc(1)",
#  "image",
#  "doc(1)(1)",
#  "doc(2)"]

# Unit test
 names = ["a(1)",
 "a(6)",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a",
 "a"]
 print(fileNaming(names))
# Expected Output = ["a(1)",
#  "a(6)",
#  "a",
#  "a(2)",
#  "a(3)",
#  "a(4)",
#  "a(5)",
#  "a(7)",
#  "a(8)",
#  "a(9)",
#  "a(10)",
#  "a(11)"]

# Unit test
 names = ["dd",
 "dd(1)",
 "dd(2)",
 "dd",
 "dd(1)",
 "dd(1)(2)",
 "dd(1)(1)",
 "dd",
 "dd(1)"]
 print(fileNaming(names))
# Expected Output = ["dd",
#  "dd(1)",
#  "dd(2)",
#  "dd(3)",
#  "dd(1)(1)",
#  "dd(1)(2)",
#  "dd(1)(1)(1)",
#  "dd(4)",
#  "dd(1)(3)"]
