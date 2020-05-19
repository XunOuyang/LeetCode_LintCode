"""
1. 这道题常规要想到的就是，从list中删除一个数字，如何做到O（1）的时间复杂度。很简单的就是，把该数字与队尾的数字进行交换。
2. 这道题最有意思的莫过于，它的follow up，每一个添加的数字，还带着权重。那么最后的random函数，需要按照权重给出结果。
这又该如何处理才能只有O（1）的时间复杂度呢？
"""
import random
class RandomizedSet(object):

    def __init__(self):
        self.nums, self.pos = [], {}
        
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop(); self.pos.pop(val, 0)
            return True
        return False
            
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]
