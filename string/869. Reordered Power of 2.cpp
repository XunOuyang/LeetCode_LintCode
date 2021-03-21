class Solution {
public:
    bool reorderedPowerOf2(int N) {
        int start = 0;
        string target = num_2_string(N);
        while(true)
        {
            if(!(pow(2, start) / pow(10, target.size() - 1)))
                start += 1;
            else if(pow(2, start) / pow(10, target.size() - 1) >= 10)
                break;
            else if(num_2_string(pow(2, start)) == target)
                return true;
            else
                start += 1;
        }        
        return false;
    }
    
    string num_2_string(int num) {
        vector<int> v;
        while(num) {
            v.push_back(num % 10);
            num /= 10;
        }
        string res = "";
        sort(v.begin(), v.end());
        for(auto& item:v) {
            res += to_string(item);
        }
        return res;
    }
};
