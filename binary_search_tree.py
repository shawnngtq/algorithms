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

    def remove(self, data):
        if not self.root:
            return False
        curr = self.root
        parent_node = None
        while curr:
            if data == curr.data:
                # 1. if no right child
                if not curr.right:
                    if not parent_node:
                        self.root = curr.left
                    else:
                        # if parent > curr, make curr left child = parent left child
                        if curr.data < parent_node.data:
                            parent_node.left = curr.left
                        # if parent < curr, make curr left child = parent right child
                        elif curr.data > parent_node.data:
                            parent_node.right = curr.left
                # 2. right child don't have left child
                elif not curr.right.left:
                    if not parent_node:
                        self.root = curr.left
                    else:
                        curr.right.left = curr.left
                        # if parent > curr, curr right child = parent left child
                        if curr.data < parent_node.data:
                            parent_node.left = curr.right
                        # if parent < curr, curr right child = parent right child
                        elif curr.data > parent_node.data:
                            parent_node.right = curr.right
                # 3. right child has left child
                else:
                    # right child's left most child
                    left_most = curr.right.left
                    left_most_parent = curr.right
                    while left_most.left:
                        left_most_parent = left_most
                        left_most = left_most.left
                    
                    # parent left subtree -> left most right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = curr.left
                    left_most.right = curr.right

                    if not parent_node:
                        self.root = left_most
                    else:
                        if curr.data < parent_node.data:
                            parent_node.left = left_most
                        elif curr.data > parent_node.data:
                            parent_node.right = left_most
                return True
            elif data < curr.data:
                parent_node = curr
                curr = curr.left
            elif data > curr.data:
                parent_node = curr
                curr = curr.right
            else:
                return "Data don't exist"


def traverse(node):
    tree = {"data": node.data}
    tree["left"] = None if not node.left else traverse(node.left)
    tree["right"] = None if not node.right else traverse(node.right)
    return tree


#       9
#   4       20
# 1 6       15  170
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
