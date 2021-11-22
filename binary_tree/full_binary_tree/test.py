# Time complexity: O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isFullTree(root):
    # Empty tree
    if root is None:
        return True

    # Leaf node
    if root.left is None and root.right is None:
        return True

    # current node has child node
    # recur the child node
    if root.left is not None and root.right is not None:
        return isFullTree(root.left) and isFullTree(root.right)

    # Otherwise, it's not full tree
    return False


root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.right = Node(40)
root.left.left = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

root.left.left.left = Node(80)
root.left.left.right = Node(90)
root.left.right.left = Node(80)
root.left.right.right = Node(90)
root.right.left.left = Node(80)
root.right.left.right = Node(90)
root.right.right.left = Node(80)
root.right.right.right = Node(90)

print("The tree is a full binary tree?: ", isFullTree(root))
