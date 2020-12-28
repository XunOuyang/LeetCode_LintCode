class Solution {
public:
    int minJumps(vector<int>& arr) {
        unordered_map<int, vector<int>> m;
        for(int i=0; i < arr.size(); i++)
        {
            m[arr[i]].push_back(i);
        }
        queue<int> q;
        vector<bool> v(arr.size(), false);
        v[0] = true;
        q.push(0);
        int res = 0;
        while(res < arr.size())
        {
            queue<int> new_q;
            while(!q.empty())
            {
                int num = q.front();
                if(num + 1 == arr.size())
                {
                    return res;
                }
                else if(!v[num + 1])
                {
                    new_q.push(num + 1);
                    v[num + 1] = true;
                }
                if(num - 1 >= 0 && !v[num-1])
                {
                    new_q.push(num - 1);
                    v[num - 1] = true;
                }
                while(!m[arr[num]].empty())
                {
                    int n = m[arr[num]].back();
                    m[arr[num]].pop_back();
                    if(!v[n])
                    {
                        new_q.push(n);
                        v[n] = true;
                    }
                }
                q.pop();
            }
            res += 1;
            q = new_q;
        }
        return arr.size();
    }
};
