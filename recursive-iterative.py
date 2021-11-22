"""
https://en.wikipedia.org/wiki/Factorial

0! = 1
5! = 5 * 4 * 3 * 2 * 1 = 120
"""


def factorialrecursive(n):
    if n < 0:
        return "only non-negative integer"
    elif 0 <= n <= 1:
        return 1
    else:
        return n * factorialrecursive(n - 1)


print("# factorialrecursive")
print(factorialrecursive(-1))
print(factorialrecursive(0))
print(factorialrecursive(1))
print(factorialrecursive(5))


def factorialiterative(n):
    if n < 0:
        return "only non-negative integer"
    elif 0 <= n <= 1:
        return 1
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output


print("# factorialiterative")
print(factorialiterative(-1))
print(factorialiterative(0))
print(factorialiterative(1))
print(factorialiterative(5))


"""
https://en.wikipedia.org/wiki/Fibonacci_number

F0 = 0, F1 = 1
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
"""


def fibonaccirecursive(n):
    if n < 0:
        return "only non-negative integer"
    if 0 <= n <= 1:
        return n
    else:
        return fibonaccirecursive(n - 1) + fibonaccirecursive(n - 2)


print("# fibonaccirecursive")
print(fibonaccirecursive(-1))
print(fibonaccirecursive(0))
print(fibonaccirecursive(1))
print(fibonaccirecursive(5))
print(fibonaccirecursive(8))


hm = {0: 0, 1: 1}


def fibonacciiterative(n):
    if n < 0:
        return "only non-negative integer"
    for i in range(2, n + 1):
        if i in hm:
            continue
        else:
            hm[i] = hm[i - 1] + hm[i - 2]
    return hm[n]


print("# fibonacciiterative")
print(fibonacciiterative(-1))
print(fibonacciiterative(0))
print(fibonacciiterative(1))
print(fibonacciiterative(5))
print(fibonacciiterative(8))
