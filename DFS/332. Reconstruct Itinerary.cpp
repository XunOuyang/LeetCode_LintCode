// 这是一道超级好的题，
// 1.DFS的思想非常的秒。两个stack左手倒腾到右手。
// 2.multiset的用法非常好。尤其是在第27行，需要注意，m[airport].erase(m[airport].begin()) 和m[airport].erase(*m[airport].begin())都是有效的，但是意义不同。
// 3. multiset 本来就是一个set里面含有多个重复的元素，既可以一次删除所有，还可以一次删除一个。
// 4. 那么，为什么这个时候我们不能够用vector<string>来代替这里的multiset呢，在下面再加上一行sort(v.begin(), v.end())，不行嘛？
// 5. 很多其他的地方是可以的，但是这里不行。map里面的vector排序完了之后又会成为乱序的，为什么呢？

class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, multiset<string>> m;
        for(auto ticket:tickets)
            m[ticket[0]].insert(ticket[1]);
        vector<string> res;
        vector<string> stack;
        
        stack.push_back("JFK");
        while(!stack.empty())
        {
            string airport = stack.back();
            if(m[airport].empty())
            {
                res.push_back(airport);
                stack.pop_back();                
            }
            else
            {
                stack.push_back(*m[airport].begin());
                m[airport].erase(m[airport].begin());
            }
        }
        return vector<string>(res.rbegin(), res.rend());
    }
};
