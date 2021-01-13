class Solution {
public:
    int numWays(int steps, int arrLen) {
        if(arrLen == 0)
            return 1;
        arrLen = min(arrLen, int(steps / 2) + 1);       // 一定要注意这一步的优化
        vector<long> pre(arrLen, 0);
        vector<long> cur(arrLen, 0);
        pre[0] = 1;
        int const mod = int(pow(10, 9) + 7);
        for(int i = 1; i < steps + 1; i++)
        {
            cur[0] = pre[0] + pre[1];
            cur[0] = cur[0] % mod;
            if(arrLen > 1)
            {
                for(int j=1; j < arrLen - 1; j++)
                {
                    cur[j] = pre[j-1] + pre[j] + pre[j+1]; 
                    cur[j] %= mod;
                }
            }
            if(arrLen)
            {
                cur[arrLen - 1] = pre[arrLen-1] + pre[arrLen - 2]; 
                cur[arrLen - 1] %= mod;
            }
            pre = cur;
        }
        return int(cur[0]);
    }
};
