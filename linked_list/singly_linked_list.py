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
    def print_length(self):
        return self.length

    # insert at root
    # O(1)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # insert at end
    # O(1)
    def append(self, data):
        new_node = Node(data)
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
    def append2(self, data):
        new_node = Node(data)
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
    def insert(self, target_node, data):
        new_node = Node(data)
        if not target_node:
            print("The target node is missing")
            return

        new_node.next = target_node.next
        target_node.next = new_node
        self.length += 1

    # insert after target by data
    # O(n)
    def insert_by_data(self, target_node_data, data):
        new_node = Node(data)
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                self.length += 1
                return
        print(f"Node with data: {target_node_data} not found")

    # insert before target by data
    # O(n)
    def insert_before_target_by_data(self, target_node_data, data):
        new_node = Node(data)
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
    def remove(self, data):
        node = self.head

        # if remove root node
        if node:
            if node.data == data:
                self.head = node.next
                self.length -= 1
                return

        while node:
            if node.data == data:
                break
            previous_node = node
            node = node.next

        if not node:
            return

        previous_node.next = node.next
        self.length -= 1

    # remove node 2
    # O(n)
    def remove2(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return

        previous_node = self.head
        for node in self:
            if node.data == data:
                previous_node.next = node.next
                self.length -= 1
                return
            previous_node = node

    def remove_all(self, data):
        dummy = Node(-1)
        dummy.next = self.head
        while dummy:
            while dummy.next and dummy.next.data == data:
                dummy.next = dummy.next.next
            dummy = dummy.next

    def reverse(self):
        if not self.head:
            return

        previous_node = None
        node = self.head
        while node:
            next_node = node.next
            node.next = previous_node
            previous_node = node
            node = next_node
        self.head = previous_node

    def remove_duplicates(self):
        node = self.head
        while node:
            while node.next and node.data == node.next.data:
                node.next = node.next.next
            node = node.next

    def middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def print_node(node):
    nodes = []
    while node:
        nodes.append(str(node.data))
        node = node.next
    nodes.append(str(None))
    return " -> ".join(nodes)


list1 = SinglyLinkedList()
list1.append(1)
list1.append(2)
list1.append(3)

print("Traverse")
list1.print_list()
print(list1)

print("Insert at root")
list1.prepend(0)
print(list1)

print("Insert at end")
list1.append(4)
print(list1)

print("Insert in the target")
list1.insert(list1.head.next.next.next, 3.5)
print(list1)

print("Remove node")
list1.remove(3.5)
print(list1)

print("Remove non-existance node")
list1.remove("img")
print(list1)

print("Insert at end 2")
list1.append2(5)
print(list1)

print("Insert after target by data")
list1.insert_by_data(3, 3.5)
print(list1)

print("Insert after target by non-existance data")
list1.insert_by_data("img", 3.5)
print(list1)

print("Insert before target by data")
list1.insert_before_target_by_data(1, 0.5)
print(list1)

print("Remove node version 2")
list1.remove2(0.5)
print(list1)

print("Remove non-existance node version 2")
list1.remove2(0.5)
print(list1)

print(f"length: {list1.length}")

list1.reverse()
print(list1)

list1.reverse()
list1.append(5)
print(list1)

list1.remove_duplicates()
print(list1)

list1.append(4)
list1.append(4)
list1.remove_all(4)
print(list1)

middle = list1.middle()
print(print_node(middle))
