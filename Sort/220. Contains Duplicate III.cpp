// 这是一道非常不容易的题目，用到了bucket sort的思想。除此以外，还有几个特别值得注意的地方：
// 1. 需要初始化判断 t 和 k
// 2. 需要考虑到是否可能溢出，所以需要用long 型
// 3. 需要考虑如果数字一旦是负数，那么所有的key的值都需要减1.
// 4. 其实也可以在m[temp] 里面存储i。
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if(t < 0 || k < 0)
            return false;
        long window = long(t) + 1;
        unordered_map<long, long> m;
        for(int i=0; i < nums.size(); i++)
        {
            long temp;
            if(nums[i] >= 0)
                temp = nums[i] / window;
            else 
                temp = nums[i] / window - 1;
            if(m.count(temp))
                return true;
            if(m.count(temp - 1) && abs(m[temp-1] - nums[i]) <= t)
                return true;
            if(m.count(temp + 1) && abs(m[temp+1] - nums[i]) <= t)
                return true;
            m[temp] = nums[i];
            if(i >= k && nums[i- k] >= 0)
                m.erase(long(nums[i-k] / window));
            else if(i >= k && nums[i- k] < 0)
                m.erase(long(nums[i-k] / window - 1));
        }
        return false;
    }
};
