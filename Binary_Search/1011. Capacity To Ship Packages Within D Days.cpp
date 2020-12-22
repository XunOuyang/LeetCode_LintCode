class Solution {
public:
    int shipWithinDays(vector<int>& weights, int D) {
        int left = weights[0], right = 0;
        for(auto& weight: weights)
        {
            left = max(weight, left);
            right += weight;
        }
        left -= 1;
        right += 1;
        while(left != right - 1)
        {
            int mid = left + (right - left) / 2;
            int count = 0;
            int temp = 0;
            for(auto& weight:weights)
            {
                if((temp + weight) <= mid)
                {
                    temp = temp + weight;
                }
                else
                {
                    temp = weight;
                    count += 1;
                }
            }
            if(count >= D)
                left = mid;
            else
                right = mid;
        }
        return right;
    }
};
