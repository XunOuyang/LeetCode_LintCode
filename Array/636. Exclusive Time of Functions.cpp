// 一道非常好的题目。尤其是值得注意的是第30行。这道题写法非常难写，如果不熟悉cpp的话。

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> res(n, 0);
        vector<int> temp(n, 0);
        vector<pair<int, int>> s;
        for(auto log:logs)
        {
            string temp1, temp2, temp3;
            int pos1, pos2;
            
            pos1 = log.find(":", 0);
            pos2 = log.find(":", pos1 + 1);
            temp1 = log.substr(0, pos1);
            temp2 = log.substr(pos1 + 1, pos2 - (pos1 + 1));
            temp3 = log.substr(pos2 + 1);
           
            if(temp2 == "start")
            {
                s.push_back(make_pair(stoi(temp1), stoi(temp3)));
            }
            else
            {
                pair<int, int> p = s.back();
                s.pop_back();
                int temp = stoi(temp3) + 1 - p.second;
                res[p.first] += temp;
                for(auto & item:s)
                {
                    item.second += temp;      
                }
            }        
        }
        return res;
    }
};
