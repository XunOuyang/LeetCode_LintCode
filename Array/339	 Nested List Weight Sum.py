class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    
    def depthSum(self, nestedList):
        # Write your code here
        self.res = 0
        self.getSum(nestedList, 1)
        return self.res
        
    def getSum(self, nestedList, layer):
        for num in nestedList:
            if num.isInteger():
                self.res += num.getInteger() * layer
            else:
                self.getSum(num.getList(), layer + 1)
