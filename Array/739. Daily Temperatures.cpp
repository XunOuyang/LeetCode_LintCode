// very similar to 901. Online Stock Span


class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size(), -1);
        vector<int> s(T.size(), -1);
        res[T.size() - 1] = 0;
        for(int i = T.size() - 1; i >= 0; i--)
        {
            int index = i + 1;
            while(index < T.size() && T[i] >= T[index])
            {
                if(res[index])
                   index += res[index];
                else
                    index = T.size();
            }
            if(index == T.size())
                res[i] = 0;
            else
                res[i] = index - i;
        }
        return res;
    }
};
