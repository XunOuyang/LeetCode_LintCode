class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() <= 1)
            return nums.size();
        int left = 1;
        int right = 1;
        while(right < nums.size())
        {  
            while(right < nums.size() && nums[right] == nums[left-1])
            {
                right++;
            }
            if(right < nums.size())
            {
                nums[left] = nums[right];
                left++;
            }
        }
        return left;
    }
};
