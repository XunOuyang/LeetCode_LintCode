class TrieNode:
    def __init__(self):
        self.end = False
        self.children = collections.defaultdict(TrieNode)

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.res = False
        self.dfs(word, self.root)
        return self.res
    
    def dfs(self, word, node):
        if not word and node.end:
            self.res = True
            return
        elif not word:
            return
        if word[0] != ".":
            node = node.children[word[0]]
            if not node:
                return
            self.dfs(word[1:], node)
        else:
            for n in node.children.values():
                self.dfs(word[1:], n)
