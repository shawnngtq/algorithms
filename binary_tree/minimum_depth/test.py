# Time complexity: O(n), traverse the tree once
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minDepth(root):
    # Corner case, should nvr hit unless root is None
    if root is None:
        return 0

    # Base case
    if root.left is None and root.right is None:
        return 1

    # If left subtree is None, recur right subtree
    if root.left is None:
        return minDepth(root.right) + 1

    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(minDepth(root))


# Level order traversal
class Node:
    # Utility to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minDepth(root):
    # Corner Case
    if root is None:
        return 0

    # Create an empty queue for level order traversal
    q = []

    # Enqueue root and initialize depth as 1
    q.append({"node": root, "depth": 1})

    # Do level order traversal
    while len(q) > 0:
        # Remove the front queue item
        queueItem = q.pop(0)

        # Get details of the removed item
        node = queueItem["node"]
        depth = queueItem["depth"]
        # If this is the first leaf node seen so far
        # then return its depth as answer
        if node.left is None and node.right is None:
            return depth

        # If left subtree is not None, add it to queue
        if node.left is not None:
            q.append({"node": node.left, "depth": depth + 1})

        # if right subtree is not None, add it to queue
        if node.right is not None:
            q.append({"node": node.right, "depth": depth + 1})


# Driver program to test above function
# Lets construct a binary tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(minDepth(root))
