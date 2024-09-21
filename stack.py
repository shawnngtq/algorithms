# LIFO
# Stack - List
class Stack:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.__dict__)

    def print_length(self):
        print(len(self.array))

    def peek(self):
        return self.array[-1]

    def push(self, data):
        self.array.append(data)
        return self.array

    def pop(self):
        self.array.pop()
        return self.array


print("# Stack - List")
s = Stack()
s.push("google")
s.push("udemy")
s.push("discord")

print("## Info")
print(s)
print(f"peek: {s.peek()}")
print(s.print_length())

print("## pop")
s.pop()
print(s)
print()


# Stack - LinkedList
# LIFO
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def __repr__(self):
        output = []
        node = self.top
        while node:
            output.append(str(node.data))
            node = node.next
        output.append("None")
        return " -> ".join(output)

    def print_length(self):
        print(self.length)

    def peek(self):
        return self.top

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        if self.length == 0:
            self.bottom = self.top
        self.length += 1

    def pop(self):
        if self.length == 0:
            return "Empty queue, pop nothing"
        else:
            output = self.top.data
            self.top = self.top.next
            self.length -= 1
            return output


print("# Stack - LinkedList")
s = Stack()
s.push("google")
s.push("udemy")
s.push("discord")

print("## Info")
print(s)
print(f"peek: {s.peek()}")
# print(s.length)
s.print_length()
print(s.top.data)
print(s.bottom.data)
# print(s.top.data)
# print(s.top.next.data)
# print(s.top.next.next.data)

print("## pop")
s.pop()
print(s)
