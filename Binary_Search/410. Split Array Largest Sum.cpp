class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long left = 0, right = 0;
        for(int num:nums)
        {
            if(num > left)
                left = num;
            right += num;
        }
        left -= 1;
        right += 1;
        while(left != right - 1)
        {
            long mid = left + (right - left) / 2;
            int count = 0;
            long s = 0;
            for(int num:nums)
            {
                if(s + num <= mid)
                {
                    s += num;
                }
                else
                {
                    s = num;
                    count += 1;
                }
            }
            if(count < m)
                right = mid;
            else
                left = mid;
        }
        return right;
    }
};
