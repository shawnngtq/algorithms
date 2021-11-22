"""
Queue - LinkedList

FIFO
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def print_length(self):
        print(self.length)

    def __repr__(self):
        output = []
        node = self.first
        while node:
            output.append(str(node.data))
            node = node.next
        output.append("None")
        return " -> ".join(output)

    def peek(self):
        return self.first

    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        if not self.first:
            return "Empty queue"
        self.first = self.first.next
        self.length -= 1
        return self


print("# Queue - LinkedList")
q = Queue()
print(q.enqueue("A"))
print(q.enqueue("B"))
print(q.enqueue("C"))
print(q.dequeue())


"""
Queue - Stack

FIFO
"""
