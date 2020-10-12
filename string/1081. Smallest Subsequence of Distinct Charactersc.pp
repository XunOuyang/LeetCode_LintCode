// Same problem as 316. Remove Duplicate Letters
// Thoughts:
// 1. count all the letters
// 2. use visited to record if a letter exist in the result or not. but even if it exists, it can be removed later.
// 3. iterate the whole string.
//    a. reduce the counter of the letter. 
//    b. if letter exist, then skip it.
//    c. if it does not exist, compare it to the previous letter, if the previous one is greater than it, and it had multiple extra left over, pop out the previous one. make the previous as not visited.
//    d. add the current to the end of the result.



class Solution {
public:
    string removeDuplicateLetters(string s) {
        string res = "";
        unordered_map<char, int> m;
        vector<char> v;
        vector<bool> visited(256, false);
        for(char c:s)
        {
            m[c]++;
        }
        for(char c:s)
        {
            m[c]--;
            if(visited[c])
                continue;
            while(v.size() > 0 && v.back() > c && m[v.back()])
            {
                visited[v.back()] = false;
                v.pop_back();
            }
            v.push_back(c);
            visited[c] = true;
        }
        for(auto c:v)
            res += c;
        return res;
    }
};
