// 一定要想清楚这是贪心法。然后第二遍遍历的时候就记得需要用max。

class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies(ratings.size(), 1);
        for(int i=0; i < ratings.size() - 1; i++)
        {
            if(ratings[i] < ratings[i+1])
                candies[i+1] = max(candies[i + 1], candies[i] + 1);
        }
        for(int i=ratings.size() - 1; i > 0; i--)
        {
            if(ratings[i] < ratings[i-1])
                candies[i-1] = max(candies[i-1], candies[i] + 1); 
        }
        return accumulate(candies.begin(), candies.end(), 0);
    }
};
