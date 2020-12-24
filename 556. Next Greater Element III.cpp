class Solution {
public:
    int nextGreaterElement(int n) {
        vector<int> v;
        long temp = long(n);
        while(n)
        {
            v.push_back(n % 10);
            n = n / 10;
        }
        int left = 0, right = 0;
        while(right < v.size() - 1)
        {
            if(v[right] > v[right + 1])
                break;
            else
                right++;
        }
        if(right == v.size() - 1)
            return -1;
        right++;
        int index = right - 1;
        while(left < right)
        {
            if(v[left] > v[right] && v[left] < v[index])
                index = left;
            left++;
        }
        swap(v[index], v[right]);
        sort(v.begin(), v.begin() + right, std::greater<>());
        temp = 0;
        while(!v.empty())
        {
            temp = temp * 10 + v.back();
            v.pop_back();
        }
        if(temp > INT_MAX)
            return -1;
        return temp;
    }
};
