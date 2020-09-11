class Solution {
public:
    string getHint(string secret, string guess) {
        if(secret.size() == 0 || secret.size() != guess.size())
            return "0A0B";
        unordered_map<char, int> s;
        unordered_map<char, int> g;
        int a = 0, b = 0;
        for(int i=0; i < secret.size(); i++)
        {
            if(secret[i] == guess[i])
                a++;
            else
            {
                s[guess[i]] > 0 ? s[guess[i]]--, b++: g[guess[i]] ++;
                g[secret[i]] > 0 ? g[secret[i]]--, b++: s[secret[i]]++;
            }
        }
        return to_string(a) + 'A' + to_string(b) + 'B';
    }
};
