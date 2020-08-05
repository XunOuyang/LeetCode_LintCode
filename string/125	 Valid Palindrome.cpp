/*
这道题三个值得注意的地方，
1. 每次遇到这种two pointer的问题，千万要注意left < right这么一个先决的判断条件
2. 一定要记得right指针是见效的
3. 要了解c++ toupper(), isalpha(), isdigit() 三个函数。
*/


class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while(left < right) {
            while(left < right && !(isalpha(s[left]) || isdigit(s[left])))
                left++;
            while(left < right && !(isalpha(s[right]) || isdigit(s[right])))
                right--;
            if(toupper(s[left++]) != toupper(s[right--]))
                return false;
        }
        return true;
    }
};
