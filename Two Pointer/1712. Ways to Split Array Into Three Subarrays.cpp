// 这道题一定要搞明白，搞清楚思路，要想到是用two pointer 来做，方向跑偏了肯定就错了。

class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        for(int i=1; i<nums.size(); i++)
        {
            nums[i] += nums[i-1];
        }
        int res = 0;
        for(int i=0, j = 0, k = 0; i < nums.size() - 2;i++)
        {
            while(j <= i || (j <= nums.size() - 2 && nums[j] - nums[i] < nums[i]))
                j++;
            while(k < j || (k < nums.size() - 1 && nums.back() - nums[k] >= nums[k] - nums[i]))
                k++;
            res = (res + k - j) % 1000000007;            
        }
        return res;
    }
};
