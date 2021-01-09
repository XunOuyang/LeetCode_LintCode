// 用C++做题一定要小心是不是可能会out of range
class Solution {
public:
    bool judgeSquareSum(int c) {
        int left = 0, right = int(pow(c, 0.5));
        while(left <= right)
        {
            long s = long(left * left) + long(right * right);
            if(s == c)
                return true;
            else if(s < c)
                left++;
            else
                right--;
        }
        return false;
    }
};
