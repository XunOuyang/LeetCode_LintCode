class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = collections.Counter(ages)
        return sum(self.request(a, b) * counter[a] * (counter[b] - (a == b)) for a in counter for b in counter )
        
        
    def request(self, a, b):
        return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
