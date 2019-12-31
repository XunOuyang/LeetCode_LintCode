class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = 0;
        for(int i=0; i<nums.size(); i++)
        {
            if(length <2 || nums[length-2] != nums[i])
            {
                nums[length++] = nums[i];
            }
        }
        return length;
    }
};
