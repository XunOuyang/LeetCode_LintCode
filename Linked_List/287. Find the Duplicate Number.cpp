class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = nums[nums[0]], slow = nums[0];
        if(nums.size() > 1) {
            while(fast != slow) {
                fast = nums[nums[fast]];
                slow = nums[slow];
            }
            fast = 0;
            while(fast != slow) {
                fast = nums[fast];
                slow = nums[slow];
            }
            return fast;
        }
        return -1;
    }
};

// using bit. 
// pay attention to the bit operation coding part.
class Solution2 {
public:
    int findDuplicate(vector<int>& nums) {
        int ret = 0;
        for(int i=0; i < 31; i++)
        {
            int a = 0;
            int b = 0;
            for(int j=0; j < nums.size(); j++)
            {
                if(nums[j] >> i & 1)
                {
                    a += 1;
                }
                if(j >> i & 1)
                {
                    b += 1;
                }
            }
            if(a > b)
            {
                ret |= 1 << i;
            }
        }
        return ret;
    }
};

// using binary search. we supposed to have n numbers smaller or equal to n.
class Solution3 {
public:
    int findDuplicate(vector<int>& nums) {
        int left = 0, right = nums.size() + 1;
        while(left != right - 1)
        {
            int mid = (right + left) / 2;
            int count = 0;
            for(int num:nums){
                if(num <= mid)
                    count += 1;
            }
            if(count > mid)
                right = mid;
            else
                left = mid;
        }
        return right;
    }
};
