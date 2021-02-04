class Solution {
public:
    int concatenatedBinary(int n) {
        long res = 0;
        long mod = 1e9 + 7;
        int bit = 0;
        for(long i=1; i <= n; i++)
        {
            bit = 0;
            while(2 << bit <= i)
                bit++;
            bit += 1;
            res = (res << bit) % mod + i;
            res %= mod;
        }
        return int(res);
    }
};
