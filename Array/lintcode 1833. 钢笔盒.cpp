class Solution {
public:
    /**
     * @param boxes: number of pens for each box
     * @param target: the target number
     * @return: the minimum boxes
     */
    int minimumBoxes(vector<int> &boxes, int target) {
        // write your code here
        unordered_map<int, int> m;
        int s = 0;
        vector<int> left(boxes.size(), INT_MAX);
        vector<int> right(boxes.size(), INT_MAX);
        int temp = INT_MAX;
        m[0] = -1;
        for(int i=0; i < boxes.size(); i++)
        {
            s += boxes[i];
            if(m.find(s - target) != m.end())
            {
                temp = min(temp, i - m[s - target]);
            }
            m[s] = i;
            left[i] = temp;
        }
        s = 0;
        m.clear();
        m[0] = boxes.size();
        temp = INT_MAX;
        for(int i = boxes.size() - 1; i >= 0; i--)
        {
            s += boxes[i];
            if(m.find(s - target) != m.end())
            {
                temp = min(temp, m[s - target] - i);
            }
            m[s] = i;
            right[i] = temp;
        }
        int res = INT_MAX;
        for(int i=0; i < boxes.size() - 1; i++)
        {
            if(left[i] == INT_MAX || right[i + 1] == INT_MAX)
                continue;
            res = min(res, (left[i]) + (right[i + 1]));
        }
        if(res == INT_MAX)
            res = -1;
        return res;
    }
};
