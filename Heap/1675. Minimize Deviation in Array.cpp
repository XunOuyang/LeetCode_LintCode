class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        priority_queue<int> pq;
        int res = INT_MAX, min_num = INT_MAX;
        for(auto& num: nums)
        {
            if(num % 2)
                num = num * 2;
            pq.push(num);
            min_num = min(min_num, num);
        }
        while(pq.top() % 2 == 0)
        {
            int temp = pq.top();
            res = min(temp - min_num, res);            
            temp = temp / 2;
            min_num = min(min_num, temp);
            pq.pop();
            pq.push(temp);
        }
        return min(abs(pq.top() - min_num), res);
    }
};
