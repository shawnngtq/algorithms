import pdb

breakpoint()


class TrieNode:
    def __init__(self) -> None:
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # https://stackoverflow.com/questions/67769308/how-to-print-trie-in-tree-structure-in-python
    def __repr__(self):
        def recur(node, indent):
            return "".join(
                indent
                + key
                + ("$" if child.is_word else "")
                + recur(child, indent + "  ")
                for key, child in node.children.items()
            )

        return recur(self.root, "\n")

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_word = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.is_word

    def startswith(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


trie = Trie()
trie.insert("test")
trie.insert("teste")
trie.insert("testing")
print(trie.search("teste"))
print(trie.search("tes"))
print(trie)
print(trie.startswith("te"))
print(trie.startswith("a"))
