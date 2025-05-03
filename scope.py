"""
Scope Resolution: When a variable is referenced inside a function, Python follows a specific order to find its definition (LEGB rule):

- Local: The current function's scope.
- Enclosing function locals: The scopes of any enclosing functions.
- Global: The module-level scope.
- Built-in: Python's built-in names.

| Feature        | global                                      | nonlocal                                               |
| -------------- | ------------------------------------------- | ------------------------------------------------------ |
| Target Scope   | Global (module-level)                       | Nearest enclosing function scope (not local or global) |
| Usage Location | Inside any function (including nested ones) | Only inside nested functions                           |
| Purpose        | Access/modify global variables              | Access/modify variables in enclosing function scopes   |
| Scope Level    | Highest level (module)                      | Intermediate levels (between local and global)         |
"""

x = 0


def outer():
    x = 1
    print(f"outer before inner: {x}")

    def inner():
        x = 2
        print(f"inner: {x}")

    inner()
    print(f"outer after inner: {x}")


print("# Without scope")
print(f"global before outer: {x}")
outer()
print(f"global after outer: {x}")
print()


def outer():
    x = 1
    print(f"outer before inner: {x}")

    def inner():
        nonlocal x
        x = 2
        print(f"inner: {x}")

    inner()
    print(f"outer after inner: {x}")


print("# nonlocal")
print(f"global before outer: {x}")
outer()
print(f"global after outer: {x}")
print()


def outer():
    x = 1
    print(f"outer before inner: {x}")

    def inner():
        global x
        x = 2
        print(f"inner: {x}")

    inner()
    print(f"outer after inner: {x}")


print("# global")
print(f"global before outer: {x}")
outer()
print(f"global after outer: {x}")
print()
