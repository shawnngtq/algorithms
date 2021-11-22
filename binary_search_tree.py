class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def print_tree(self):
        if self.root:
            return self.traverse(self.root)

    def traverse(self, node):
        tree = {"data": node.data}
        tree["left"] = None if not node.left else traverse(node.left)
        tree["right"] = None if not node.right else traverse(node.right)
        return tree

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            curr = self.root
            while curr:
                if data < curr.data:
                    if not curr.left:
                        curr.left = new_node
                        return
                    curr = curr.left
                else:
                    if not curr.right:
                        curr.right = new_node
                        return
                    curr = curr.right
        return self

    def lookup(self, data):
        if not self.root:
            return "Empty tree"
        else:
            curr = self.root
            while curr:
                if data == curr.data:
                    return curr
                elif data < curr.data:
                    curr = curr.left
                elif data > curr.data:
                    curr = curr.right
                else:
                    return "Data don't exist"


def traverse(node):
    tree = {"data": node.data}
    tree["left"] = None if not node.left else traverse(node.left)
    tree["right"] = None if not node.right else traverse(node.right)
    return tree


#   9
#   4   20
# 1 6   15  170
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree.print_tree())
# print(traverse(tree.root))
print(tree.lookup(170).data)
print(tree.lookup(50))
print(tree.lookup(-1))
