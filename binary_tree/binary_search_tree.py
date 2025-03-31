# full binary tree - all the nodes have 0 or two children
# complete binary tree - all the levels are completely filled
# binary tree vs binary search tree - https://www.geeksforgeeks.org/difference-between-binary-tree-and-binary-search-tree/


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
        tree["left"] = None if not node.left else self.traverse(node.left)
        tree["right"] = None if not node.right else self.traverse(node.right)
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

    def breadth_first_search(self):
        output, queue = [], []
        curr = self.root
        queue.append(curr)
        while queue:
            curr = queue.pop(0)
            output.append(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return output

    def breadth_first_search_recursive(self, output, queue):
        if not queue:
            return output
        curr = queue.pop(0)
        output.append(curr.data)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        return self.breadth_first_search_recursive(output, queue)

    # def depth_in_order(self, node, output):
    #     if not node:
    #         return output
    #     if node.left:
    #         return self.depth_in_order(node.left, output)
    #     output.append(node.data)
    #     if node.right:
    #         return self.depth_in_order(node.right, output)

    def depth_first_search_in_order(self, node, output):
        def traverse_in_order(node, output):
            if node.left:
                traverse_in_order(node.left, output)
            output.append(node.data)
            if node.right:
                traverse_in_order(node.right, output)
            return output

        return traverse_in_order(node, output)

    def depth_first_search_post_order(self, node, output):
        def traverse_post_order(node, output):
            if node.left:
                traverse_post_order(node.left, output)
            if node.right:
                traverse_post_order(node.right, output)
            output.append(node.data)
            return output

        return traverse_post_order(node, output)

    def depth_first_search_pre_order(self, node, output):
        def traverse_pre_order(node, output):
            output.append(node.data)
            if node.left:
                traverse_pre_order(node.left, output)
            if node.right:
                traverse_pre_order(node.right, output)
            return output

        def traverse_pre_order(node, output):
            if node:
                output.append(node.data)
                traverse_pre_order(node.left, output)
                traverse_pre_order(node.right, output)
            return output

        return traverse_pre_order(node, output)

    def depth(self):
        def dfs(node, number):
            if not node:
                return number
            else:
                return max(dfs(node.left, number + 1), dfs(node.right, number + 1))

        node = self.root
        return dfs(node, 0)


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

print(f"tree: {tree.print_tree()}")
print(f"170 exists: {tree.lookup(170).data}")
print(f"50 exists: {tree.lookup(50)}")
print(f"-1 exists: {tree.lookup(-1)}")
print(f"breadth first search: {tree.breadth_first_search()}")
print(
    f"breadth first search recursive: {tree.breadth_first_search_recursive([], [tree.root])}"
)
print(f"depth first search in order: {tree.depth_first_search_in_order(tree.root, [])}")
print(
    f"depth first search post order: {tree.depth_first_search_post_order(tree.root, [])}"
)
print(
    f"depth first search pre order: {tree.depth_first_search_pre_order(tree.root, [])}"
)
print(tree.depth())
