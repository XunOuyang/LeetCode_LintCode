import bisect
import collections
class Solution:
    def alienOrder(self, words):
        # Write your code here
        res = []
        d = collections.defaultdict(list)
        indegree = dict()
        letters = set()
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    d[words[i][j]].append(words[i+1][j])
                    indegree[words[i+1][j]] = indegree.get(words[i+1][j], 0) + 1
                    indegree[words[i][j]] = indegree.get(words[i][j], 0)
                    break
        
        for word in words:
            for c in word:
                letters.add(c)
        
        q = collections.deque()
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)
        res = []
        if not q:
            return ""
        while q:
            node = q.popleft()
            res.append(node)
            letters.remove(node)
            for item in d[node]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    q.append(item)
        for key in indegree:
            if indegree[key] != 0:
                return ""
        letters = list(letters)
        for letter in letters:
            bisect.insort(res, letter)
        return "".join(res)
