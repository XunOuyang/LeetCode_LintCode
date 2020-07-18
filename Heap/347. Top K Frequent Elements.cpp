class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> m;                          //注意map初始化的写法
        priority_queue<pair<int, int>> pq;        //注意pq 初始化的写法，即使里面用的是pair，也会按照第一个的值根据大小来，而且用top来调用最大的。
        vector<int> res;
        for(int num:nums)
        {
            m[num] += 1;
        }
        for(auto it=m.begin(); it!= m.end(); it++)
            pq.push(make_pair(it->second, it->first));      //注意，由于it 是iterator，所以调用要用->，而且pair里面第一个元素或者第二个，后面没有括号。
        while(k)
        {
            k -= 1;
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};
