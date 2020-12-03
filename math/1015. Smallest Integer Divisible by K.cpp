class Solution {
public:
    int smallestRepunitDivByK(int K) {
        unordered_set<int> s{1, 3, 7, 9};
        if(s.count(K % 10) == 0)
            return -1;
        int res = 0;
        int num = 0;
        do
        {
            num = num * 10 + 1;
            num = num % K;
            res++;
        }while(num != 0);
        return res;
    }
};
