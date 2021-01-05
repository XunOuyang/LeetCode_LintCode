// 这道题不需要前后加两个元素，只需要前后各加一个元素就行了
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if(!n)
            return true;
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);
        for(int i=1; i < flowerbed.size() - 1; i++)
        {
            if(flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0)
            {
                n -= 1;
                flowerbed[i] = 1;
            }
            if(!n)
                break;
        }
        return n == 0;
    }
};
