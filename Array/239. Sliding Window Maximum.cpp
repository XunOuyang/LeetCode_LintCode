Python:
```
import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k == 1:
            return nums
        dq = collections.deque()
        res = []
        for i in range(len(nums)):
            while dq and nums[i] > dq[-1][0]:
                dq.pop()
            dq.append([nums[i], i])
            if i - k >= dq[0][1]:
                dq.popleft()
            if i - k >= -1:
                res.append(dq[0][0])
        return res
```
                
这道题没有必要deque里面push进去一对数据，只需要数组数据的index即可。
C++:
```
#include <deque>
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> res;
        if(nums.size() == 0 || k == 1)
            return nums;
        for(int i=0; i<nums.size(); i++) {
            while(!dq.empty() && nums[dq.back()] <= nums[i])
                dq.pop_back();
            dq.push_back(i);
            if(dq.front() == i - k)
                dq.pop_front();
            if(i - k >= -1)
                res.push_back(nums[dq.front()]);
        }
        return res;
    }
};
```
