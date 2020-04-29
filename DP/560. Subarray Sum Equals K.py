"""
这道题看起来代码就一小戳。但是其实这样的表达非常难。
难点在于，利用的一直都是差值！所以才会有d = {0:1}，然后特别需要注意d[s] = d.get(s, 0) + 1要放在res 的update之后。
如果不这样的话，也可以改成solution 2 或者3.
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        res = 0
        d = {0:1}
        for num in nums:
            s += num
            res += d.get(s-k, 0)
            d[s] = d.get(s, 0)+1
        return res
    
class Solution2(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        res = 0
        d = dict()
        nums = [0] + nums
        for num in nums:
            s += num
            res += d.get(s-k, 0)
            d[s] = d.get(s, 0)+1
        return res
    
class Solution3(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running_sum = 0
        hash_table = collections.defaultdict(lambda:0)
        total = 0
        for x in nums:
            running_sum += x
            sum = running_sum - k
            if sum in hash_table:
                total += hash_table[sum]
            if running_sum == k:
                total += 1
            hash_table[running_sum] += 1
        return total
