// 最简单的双指针，居然提交这么多次不通过。注意细节。
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int res = 0;
        int left = 0, right = people.size() - 1;
        while(left <= right)
        {
            res++;
            int temp = limit;
            temp -= people[right--];
            if(left <= right && temp >= people[left])
                temp -= people[left++];         
        }
        return res;
    }
};
