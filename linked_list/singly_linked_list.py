# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # traverse = iterate
    # `for node in self` won't work without this
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # https://realpython.com/linked-lists-python/
    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append(str(None))
        return " -> ".join(nodes)

    # traversing
    # 0(n)
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # O(1)
    def length(self):
        return self.length

    # insert at root
    # O(1)
    def prepend(self, new_node):
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # insert at end
    # O(1)
    def append(self, new_node):
        if not self.head:
            self.head = new_node
            self.length += 1
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        self.length += 1

    # insert at end (version 2)
    # O(1)
    # this is possible due to __iter__
    def append2(self, new_node):
        if not self.head:
            self.head = new_node
            self.length += 1
            return

        for node in self:
            pass
        node.next = new_node
        self.length += 1

    # insert after target
    # O(n)
    def insert(self, target_node, new_node):
        if not target_node:
            print("The target node is missing")
            return

        new_node.next = target_node.next
        target_node.next = new_node
        self.length += 1

    # insert after target by data
    # O(n)
    def insert_by_data(self, target_node_data, new_node):
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                self.length += 1
                return
        print(f"Node with data: {target_node_data} not found")

    # insert before target by data
    # O(n)
    def insert_before_target_by_data(self, target_node_data, new_node):
        if not self.head:
            self.length += 1
            return self.prepend(new_node)

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = new_node
                new_node.next = node
                self.length += 1
                return
            previous_node = node
            self.length += 1

    # remove node
    # O(n)
    def remove(self, target_node_data):
        node = self.head

        # if remove root node
        if node:
            if node.data == target_node_data:
                self.head = node.next
                self.length -= 1
                return

        while node:
            if node.data == target_node_data:
                break
            previous_node = node
            node = node.next

        if not node:
            return

        previous_node.next = node.next
        self.length -= 1

    # remove node 2
    # O(n)
    def remove2(self, target_node_data):
        if self.head.data == target_node_data:
            self.head = self.head.next
            self.length -= 1
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                self.length -= 1
                return
            previous_node = node


list1 = SinglyLinkedList()
list1.head = Node(1)
node2 = Node(2)
node3 = Node(3)
list1.head.next = node2
node2.next = node3

print("Traverse")
list1.print_list()
print(list1)

print("Insert at root")
list1.prepend(Node(0))
print(list1)

print("Insert at end")
list1.append(Node(4))
print(list1)

print("Insert in the target")
list1.insert(list1.head.next.next.next, Node(3.5))
print(list1)

print("Remove node")
list1.remove(3.5)
print(list1)

print("Remove non-existance node")
list1.remove("img")
print(list1)

print("Insert at end 2")
list1.append2(Node(5))
print(list1)

print("Insert after target by data")
list1.insert_by_data(3, Node(3.5))
print(list1)

print("Insert after target by non-existance data")
list1.insert_by_data("img", Node(3.5))
print(list1)

print("Insert before target by data")
list1.insert_before_target_by_data(1, Node(0.5))
print(list1)

print("Remove node version 2")
list1.remove2(0.5)
print(list1)

print("Remove non-existance node version 2")
list1.remove2(0.5)
print(list1)

print("length")
list1.length()
