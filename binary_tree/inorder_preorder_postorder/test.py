class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# print inorder tree traversal
def inorderPrint(root):
  if root:

    # 1st recur on the left child
    inorderPrint(root.left)

    # then on Node
    print(root.data)

    # right child
    inorderPrint(root.right)

# print preorder tree traversal
def preorderPrint(root):
  if root:
    print(root.data)
    preorderPrint(root.left)
    preorderPrint(root.right)

# print postorder tree traversal
def postorderPrint(root):
  if root:
    postorderPrint(root.left)
    postorderPrint(root.right)
    print(root.data)


# test code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Inorder traversal of BT is:')
inorderPrint(root)

print('Preorder traversal of BT is:')
preorderPrint(root)

print('Postorder traversal of BT is:')
postorderPrint(root)