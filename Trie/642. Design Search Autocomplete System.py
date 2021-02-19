import collections

class TrieNode:
    def __init__(self):
        self.sentence = set()
        self.children = collections.defaultdict(TrieNode)
        
class Solution:
    def __init__(self, sentences, frequencies):
        self.root = TrieNode()
        self.frequencies = dict()
        for i in range(len(sentences)):
            self.frequencies[sentences[i]] = frequencies[i]
            self.addSentence(sentences[i], frequencies[i])
            
    def search(self, word):
        node = self.root
        res = []
        for c in word:
            node = node.children[c]
        temp = list(node.sentence)
        temp.sort(reverse=True, key=lambda x:self.frequencies[x])
        for i in range(min(3, len(temp))):
            res.append(temp[i])
        return res
            
            
    def addSentence(self, sentence, frequencies):
        node = self.root
        for c in sentence:
            node = node.children[c]
            node.sentence.add(sentence)
            
sentences = ["aaa", "aab", "aac"]
times = [3,1,2]
a = Solution(sentences, times)
print(a.search("aa"))
