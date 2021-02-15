class Solution {
public:
    /**
     * @param sticks: the length of sticks
     * @return: Minimum Cost to Connect Sticks
     */
    int MinimumCost(vector<int> &sticks) {
        // write your code here
        if(sticks.size() < 1)
            return 0;
        priority_queue<int> pq;
        for(auto& stick:sticks)
            pq.push(-stick);
        int res = 0;
        while(pq.size() != 1)
        {
            int a = -pq.top();
            pq.pop();
            int b = -pq.top();
            pq.pop();
            res += a + b;
            pq.push(-(a + b));
        }
        return res;
    }
};
