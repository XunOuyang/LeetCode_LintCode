class TrieNode():
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
        return self.dfs(word, self.root, 0)
    
    
    def dfs(self, word, node, i):
        if i == len(word):
            return node.end
        if word[i] == '.':
            for item in node.children:
                if self.dfs(word, node.children[item], i + 1):
                    return True
        elif word[i] in node.children:
            node = node.children[word[i]]
            return self.dfs(word, node, i + 1)
        else:
            return False
        
