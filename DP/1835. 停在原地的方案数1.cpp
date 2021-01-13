class Solution {
public:
    /**
     * @param steps: steps you can move
     * @param arrLen: the length of the array
     * @return: Number of Ways to Stay in the Same Place After Some Steps
     */
    int numWays(int steps, int arrLen) {
        // write your code here
        if(arrLen == 0)
            return 1;
        vector<int> pre(arrLen, 0);
        vector<int> cur(arrLen, 0);
        pre[0] = 1;
        for(int i = 1; i < steps + 1; i++)
        {
            cur[0] = pre[0] + pre[1];
            if(arrLen > 1)
            {
                for(int j=1; j < arrLen - 1; j++)
                {
                    cur[j] = pre[j-1] + pre[j] + pre[j+1]; 
                }
            }
            if(arrLen)
                cur[arrLen - 1] = pre[arrLen-1] + pre[arrLen - 2]; 
            pre = cur;
        }
        return cur[0] % int(pow(10, 9) + 7);
    }
};
