class Solution {
public:
    /**
     * @param stations: an integer array
     * @param k: an integer
     * @return: the smallest possible value of D
     */
    double minmaxGasDist(vector<int> &stations, int k) {
        // Write your code here
        sort(stations.begin(), stations.end());
        double left = 0, right = stations.back() - stations[0];
        int count;
        while(left < right - 10e-6)
        {
            count = 0;
            double mid = (left + right) / 2;
            for(int i = 0; i < stations.size() - 1; i++)
            {
                if(stations[i+1] - stations[i] > mid)
                {
                    count += ceil((stations[i+1] - stations[i])/mid) - 1;
                }
            }
            if(k < count)           // mid too small
                left = mid;
            else
                right = mid;
        }
        return right;
    }
};
