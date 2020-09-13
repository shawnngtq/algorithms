# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # https://realpython.com/linked-lists-python/
    def __repr__(self):
        node = self.head
        nodes = []
        while (node):
            nodes.append(str(node.data))
            node = node.next
        nodes.append(str(None))
        return " -> ".join(nodes)

    # traversing
    def list_print(self):
        node = self.head
        while (node):
            print(node.data)
            node = node.next

    # traverse = iterate
    # `for node in self` won't work without this
    def __iter__(self):
        node = self.head
        while (node):
            yield node
            node = node.next

    # insert at root
    def insert_root(self, new_node):
        new_node.next = self.head
        self.head = new_node

    # insert at end
    def insert_end(self, new_node):
        if not self.head:
            self.head = new_node
            return

        node = self.head
        while (node.next):
            node = node.next

        node.next = new_node

    # insert at end (version 2)
    def insert_end2(self, new_node):
        if not self.head:
            self.head = new_node
            return

        for node in self:
            pass

        node.next = new_node

    # insert after target
    def insert_after_target(self, target_node, new_node):
        if not target_node:
            print("The target node is missing")
            return

        new_node.next = target_node.next
        target_node.next = new_node

    # insert after target by data
    def insert_after_target_by_data(self, target_node_data, new_node):
        for node in self:
            if (node.data == target_node_data):
                new_node.next = node.next
                node.next = new_node
                return
        print(f"Node with data: {target_node_data} not found")

    # insert before target by data
    def insert_before_target_by_data(self, target_node_data, new_node):
        if not self.head:
            return self.insert_root(new_node)

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = new_node
                new_node.next = node
                return
            previous_node = node

    # remove node
    def remove_node(self, target_node_data):
        node = self.head

        # if remove root node
        if node:
            if (node.data == target_node_data):
                self.head = node.next
                return

        while (node):
            if (node.data == target_node_data):
                break
            previous_node = node
            node = node.next

        if not node:
            return

        previous_node.next = node.next

    # remove node 2
    def remove_node2(self, target_node_data):
        if (self.head.data == target_node_data):
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if (node.data == target_node_data):
                previous_node.next = node.next
                return
            previous_node = node


list1 = SinglyLinkedList()
list1.head = Node(1)
node2 = Node(2)
node3 = Node(3)
list1.head.next = node2
node2.next = node3

print("Traverse")
list1.list_print()

print("Insert at root")
list1.insert_root(Node(0))
print(list1)

print("Insert at end")
list1.insert_end(Node(4))
print(list1)

print("Insert in the target")
list1.insert_after_target(list1.head.next.next.next, Node(3.5))
print(list1)

print("Remove node")
list1.remove_node(3.5)
print(list1)

print("Remove non-existance node")
list1.remove_node("img")
print(list1)

print("Insert at end 2")
list1.insert_end2(Node(5))
print(list1)

print("Insert after target by data")
list1.insert_after_target_by_data(3, Node(3.5))
print(list1)

print("Insert after target by non-existance data")
list1.insert_after_target_by_data("img", Node(3.5))
print(list1)

print("Insert before target by data")
list1.insert_before_target_by_data(1, Node(0.5))
print(list1)

print("Remove node version 2")
list1.remove_node2(0.5)
print(list1)

print("Remove non-existance node version 2")
list1.remove_node2(0.5)
print(list1)
