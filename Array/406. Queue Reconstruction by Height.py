class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key=lambda x:(x[0], -x[1]))
        while people:
            [h, k] = people.pop()
            res.insert(k, [h, k])
        return res
