/*
Question:  There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of   painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses 
have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
*/

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if(costs.size() == 0 || costs[0].size() == 0)
            return 0;
        vector<vector<int>> dp = costs;
        for(int i=1; i<costs.size(); i++)
            for(int j=0; j<costs[0].size(); j++) {
                dp[i][j] += min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]);  
            }
        return min(dp[costs.size()-1][0], min(dp[costs.size()-1][1], dp[costs.size()-1][2]));
    }
};

// Comment: dp[costs.size()-1][0] can be replaced by dp.back()[0]
