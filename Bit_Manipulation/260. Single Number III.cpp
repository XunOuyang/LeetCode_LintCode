class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int key = 0;
        for(int num:nums)
            key ^= num;
        vector<int> A, B, res;
        int n = 0;
        while(key % 2 == 0)
        {
            key /= 2;
            n += 1;
        }
        int x = pow(2, n);
        for(int num:nums)
        {
            if((num ^ key) & x)
                A.push_back(num);
            else
                B.push_back(num);
        }
        key = 0;
        for(int num:A)
            key ^= num;
        res.push_back(key);
        key = 0;
        for(int num:B)
            key ^= num;
        res.push_back(key);
        return res;
    }
};
