class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> m;
        int max_q = 0;
        for(char task:tasks)
        {
            m[task] += 1;
            max_q = max(m[task], max_q);
        }
        int q = 0;
        for(auto item:m)
        {
            if(item.second == max_q)
                q += 1;
        }
        return max(int(tasks.size()), (max_q - 1) * (n + 1) + q);
    }
};
