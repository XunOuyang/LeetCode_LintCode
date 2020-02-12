// A very good question. Cannot use recursion directly. So we need to create a wrapper first. 
//We need to understand what the wrapper looks like. What do we want to add to the wrapper. The return condition.
// Also, please understand do not mix the code below, I made mistakes here when I first tried to approach this problem.

```
while(n-->0) {

}
```
The code above is different than the code below:
```
while(n) {
    n--;
}
```
```
class Solution {
public:
    string decodeString(string s) {
        int pos = 0;
        return decodeString(s, pos);
    }
    
    string decodeString(string s, int& i) {
        string res = "";
        int n = 0;
        for(; i < s.size(); i++) {
            if(s[i] == '[') {
                string temp = decodeString(s, ++i);
                while(n) {
                    res += temp;
                    n--;
                }
            } 
            else if (isdigit(s[i])) 
                n = n*10 + s[i] - '0';
            else if(s[i] == ']')
                return res;
            else
                res += s[i];
        }
        return res;
    }
};
```
