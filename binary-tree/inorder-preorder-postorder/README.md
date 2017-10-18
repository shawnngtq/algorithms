## [Tree Traversals (Inorder, Preorder and Postorder)](http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)

__Inorder Traversal (Left, Root, Right)__:
1. Traverse the left subtree, i.e., call Inorder(left-subtree)
2. Visit the root.
3. Traverse the right subtree, i.e., call Inorder(right-subtree)

In case of binary search trees (BST), inorder traversal gives nodes in non-decreasing order.

__Preorder Traversal (Root, Left, Right)__:
1. Visit the root.
2. Traverse the left subtree, i.e., call Preorder(left-subtree)
3. Traverse the right subtree, i.e., call Preorder(right-subtree)

Preorder traversal is used to create a copy of the tree.

__Postorder Traversal (Left, Right, Root)__:
1. Traverse the left subtree, i.e., call Postorder(left-subtree)
2. Traverse the right subtree, i.e., call Postorder(right-subtree)
3. Visit the root.

Postorder traversal is used to delete the tree.