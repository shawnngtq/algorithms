class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def print_tree(self):
        print(self.data)
