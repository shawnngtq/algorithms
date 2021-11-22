# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def in_order_traversal(self, root):
        """left -> root -> right"""
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.data)
            res += self.in_order_traversal(root.right)
        return res

    def pre_order_traversal(self, root):
        """root -> left -> right"""
        res = []
        if root:
            res.append(root.data)
            res += self.pre_order_traversal(root.left)
            res += self.pre_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        """left -> right -> root"""
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res += self.post_order_traversal(root.right)
            res.append(root.data)
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insert(20)

print("Print tree:")
root.print_tree()

print("In order traversal:")
print(root.in_order_traversal(root))

print("Pre order traversal:")
print(root.pre_order_traversal(root))

print("Post order traversal:")
print(root.post_order_traversal(root))
