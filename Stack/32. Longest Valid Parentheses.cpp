// 这道题解法非常多。左右两边两遍的扫描才是最好的解法。
class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> v;
        int res = 0;
        for(auto& c:s) {
            if(c == '(') {
                v.push_back(1);
            }
            else {
                if(!v.empty()) {
                    int temp = 0;
                    while(!v.empty() && v.back() != 1) {
                        temp += v.back();
                        v.pop_back();
                    }
                    if(!v.empty()) {
                        v.back() = v.back() + 1 + temp;
                        res = max(res, v.back());
                    }
                    else {
                        res = max(res, temp);
                    }
                }
            }
        }
        int temp = 0;
        for(auto& num:v) {
            if(num % 2 == 0) {
                temp += num;
                res = max(res, temp);
            }
            else {
                temp = 0;
            }
        }
        return res;
    }
};
