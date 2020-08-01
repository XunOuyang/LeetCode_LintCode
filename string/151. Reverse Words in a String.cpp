/* 这是一道非常容易的题，理论上没有任何刷题基础都应该能够做出来。除了要知道s.resize(x)的用法以外，最主要是做提前要把思路理清楚。
1. 取得每一个单词的第一个字母的位置
2. 取得每一个单词最后一个字母的位置
3. 复制这个单词到正确的位置（每两个单词之间只能留有一个空格）
4. 将该单词反转
5.重复1到4直到所有的单词都走完为止。


class Solution {
public:
    void reverseString(string& s, int start, int end) {
        while(start < end) {
            char temp = s[start];
            s[start++] = s[end];
            s[end--] = temp;
        }
    }
    
    string reverseWords(string s) {
        int i = 0, j = 0;
        int length = s.size();
        int wordcount = 0;
        while(true)
        {
            while(s[i] == ' ')
                i++;
            if(i == length)
                break;
            int l = 0;
            if(wordcount)
            {
                s[j++] = ' ';
            }
            while(i < length && s[i] != ' ')
            {
                s[j] = s[i];
                j++;
                i++;
                l++;
            }
            reverseString(s, j-l, j-1);
            wordcount++;
        }
        s.resize(j);
        reverseString(s, 0, j-1);
        return s;
    }
};
