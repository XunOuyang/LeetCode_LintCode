class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int res = 0;
        for(auto num:nums)
        {
            if(num > 5) {
                vector<int> temp;
                temp = getDivisors(num);
                if(temp.size() == 4)
                    res += accumulate(temp.begin(), temp.end(), 0);
            }
        }
        return res;
    }
    
    vector<int> getDivisors(int num) {
        vector<int> v;
        for(int i=1; i <= floor(sqrt(num)); i++) {
            if(num % i == 0)
            {
                v.push_back(i);
                if(i != num / i)
                    v.push_back(num / i);
            }
        }
        return v;
    }
};
