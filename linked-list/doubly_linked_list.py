class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while (node):
            nodes.append(str(node.data))
            node = node.next
        nodes.append(str(None))
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while (node):
            yield node
            node = node.next

    # push is queue, FIFO
    def push(self, new_node):
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # insert
    def insert_after(self, target_node_data, new_node):
        for node in self:
            if (node.data == target_node_data):
                new_node.next = node.next
                node.next = new_node
                new_node.prev = node
                if new_node:
                    new_node.next.prev = new_node

    # append is stack, LIFO
    def append(self, new_node):
        if not self.head:
            self.head = new_node
            return
        node = self.head
        while (node.next):
            node = node.next
        node.next = new_node
        new_node.prev = node


print("Initialize")
list1 = DoublyLinkedList()
list1.push(Node(1))
list1.push(Node(2))
list1.push(Node(3))
print(list1)

print("Insert after")
list1.insert_after(2, Node(4))
print(list1)

print("Insert after non-existance value")
list1.insert_after("img", Node(4))
print(list1)

print("Append")
list1.append(Node(5))
print(list1)
