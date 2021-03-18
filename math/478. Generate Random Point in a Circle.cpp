// 这道题两个需要注意的点：
// 1. 理解需要用到 a^2 + b^2 <= r^2。
// 2. 用 do while 的结构
// 3. RAND_MAX

class Solution {
public:
    double r, _x, _y;
    Solution(double radius, double x_center, double y_center) {
        r = radius;
        _x = x_center;
        _y = y_center;
    }
    
    vector<double> randPoint() {
        double x, y;
        do{
            x = (2 * ((float)rand() / RAND_MAX) - 1) * r;
            y = (2 * ((float)rand() / RAND_MAX) - 1) * r;
        } while(x * x + y * y > r * r);
        return {x + _x, y + _y};                
    }
};
