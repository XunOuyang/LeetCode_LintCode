class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int buy = prices[0], sell = 0, res = 0;
        for(int i=1; i < prices.size(); i++)
        {
            if(sell == 0 && prices[i] < buy)
                buy = prices[i];
            else if(sell == 0 && prices[i] <= buy + fee)
                continue;
            else if(sell == 0 && prices[i] > buy + fee)
            {
                sell = prices[i];
            }
            else if(sell > 0 && prices[i] >= sell - fee)
            {
                sell = max(sell, prices[i]);
            }
            else if(sell > 0 && prices[i] < sell - fee)
            {
                res += sell - buy - fee;
                buy = prices[i];
                sell = 0;
            }
        }
        if(sell > 0)
            res += sell - buy - fee;
        return res;
    }
};
