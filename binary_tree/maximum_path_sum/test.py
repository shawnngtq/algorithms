class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findMaxPath(root):

    # Base case, leaf node
    if root is None:
        return 0

    # l and r storing the max path sum going thr
    # left and right child of root respectively
    l = findMaxPath(root.left)
    r = findMaxPath(root.right)

    # Max path for parent call of root. This path
    # must include at most one child of root
    max_single = max(max(l, r) + root.data, root.data)

    # max_top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    max_top = max(max_single, l + r + root.data)

    # Static variable to store the changes
    # Store the maximum result
    findMaxPath.res = max(findMaxPath.res, max_top)

    return max_single


def findMaxSum(root):
    # Initialize result
    findMaxPath.res = float("-inf")

    # Compute and return result
    findMaxPath(root)
    return findMaxPath.res


root = Node(10)
root.left = Node(-2)
root.right = Node(10)
print("Max path sum is ", findMaxSum(root))

root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print("Max path sum is ", findMaxSum(root))
