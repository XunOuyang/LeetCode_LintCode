class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int temp = 1, res = 0;
        int cur = nums[0];
        bool up = true;
        for(int i=1; i < nums.size();i++)
        {
            if(nums[i] > cur && up)
            {
                up = false;
                cur = nums[i];
                temp += 1;
            }
            else if(nums[i] > cur)
            {
                cur = nums[i];
            }
            else if(nums[i] < cur && !up)
            {
                up = true;
                cur = nums[i];
                temp += 1;
            }
            else if(nums[i] < cur)
            {
                cur = nums[i];
            }
        }
        res = max(res, temp);
        cur = nums[0];
        up = false;
        temp = 1;
        for(int i=1; i < nums.size();i++)
        {
            if(nums[i] > cur && up)
            {
                up = false;
                cur = nums[i];
                temp += 1;
            }
            else if(nums[i] > cur)
            {
                cur = nums[i];
            }
            else if(nums[i] < cur && !up)
            {
                up = true;
                cur = nums[i];
                temp += 1;
            }
            else if(nums[i] < cur)
            {
                cur = nums[i];
            }
        }
        res = max(res, temp);
        return res;
    }
};
