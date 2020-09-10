// 这道题特别需要注意的是，C++里面跟python很不同。如果需要把一个字母变成数字，那么需要给类型符号外面加上括号。
// 而(int)'1'，不是把字符‘1’变成数字1，而是把字符'1'的ascii value取出来。
class Solution {
public:
    int compareVersion(string version1, string version2) {
        int num1 = 0, num2 = 0;
        int i = 0, j = 0;
        while(i < version1.size() || j < version2.size())
        {
            while(i < version1.size() && version1[i] != '.')
            {
                num1 = num1 * 10 + version1[i] - '0';                
                i++;
            }
            while(j < version2.size() && version2[j] != '.')
            {
                num2 = num2 * 10 + version2[j] - '0';
                j++;
            }
            if(num1 < num2)
                return -1;
            else if(num1 > num2)
                return 1;
            num1 = 0;
            num2 = 0;
            i++;
            j++;
        }
        return 0;
    }
};
