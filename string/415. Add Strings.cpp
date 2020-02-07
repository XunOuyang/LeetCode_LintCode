// This is a very good question, actually there can be one more follow up -- 
// What if there can be negative numbers ? 

class Solution {
public:
    string addStrings(string num1, string num2) {
        int val = 0, carry = 0;
        string res = "";
        int i = num1.size()-1, j = num2.size()-1;
        while(i >= 0 || j >= 0)
        {
            while(i >= 0 && j >= 0)
            {
                int a = num1[i] - '0';
                int b = num2[j] - '0';
                val = a + b + carry;
                carry = val/10;
                val = val%10;
                res += std::to_string(val);
                val = 0;
                i--;
                j--;
            }
            while(i >= 0)
            {
                int a = num1[i] - '0';
                val = a + carry;
                carry = val/10;
                val = val%10;
                res += std::to_string(val);
                val = 0;
                i--;
            }
            while(j >= 0)
            {
                int b = num2[j] - '0';
                val = b + carry;
                carry = val/10;
                val = val%10;
                res += std::to_string(val);
                val = 0;
                j--;
            }
        }
        if(carry)
            res += std::to_string(carry);
        reverse(res.begin(), res.end());
        return res;
    }
};
