class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if(t < 0 || k < 0)
            return false;
        unordered_map<long int, long int> m;
        long int window = long(t) + 1;
        for(int i=0; i<nums.size(); i++)
        {
            long int temp;
            if(nums[i] >=0 )
                temp = nums[i] / window;
            else
                temp = nums[i] / window - 1;
            //cout << temp << endl;
            if(m.count(temp))
                return true;
            if(m.count(temp - 1) && abs(m[temp-1] - nums[i]) <= t)
            {
                //cout << "asdf1" << endl;
                return true;
            }
            if(m.count(temp + 1) && abs(m[temp+1] - nums[i]) <= t)
            {
                //cout << m[temp+1] << nums[i] << endl;
                return true;
            }
            //m.insert(pair<int, int>(temp, nums[i]));
            m[temp] = nums[i];
            if(i >= k)
                m.erase(int(nums[i-k] / window));
        }
        return false;
    }
};
