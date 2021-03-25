// 这道题，非常微妙，非常不好写。
// 为什么，因为会出现需要用multi set 的情况，所以其实不能用 WrongSolution 里面的解法来的，会有重复的数字。
// 这个写法又有一个特别需要注意的地方。set 里面有erase(）方法，但是这里我们需要erase iterator，而不是那个值。
// 因为那个值可能有多个，如果erase了一次，所有的都被抹去了。
class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        multiset<int> s(A.begin(), A.end());
        for(int i=0; i < A.size(); i++)
        {
            auto pos = upper_bound(s.begin(), s.end(), B[i]);
            if(pos == s.end()) {
                pos = s.begin();                
            }
            A[i] = *pos;
            s.erase(pos);
        }
        return A;
    }
};




class WrongSolution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        vector<int> C =B;
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());
        unordered_map<int, int> m;
        int left = 0, right = A.size() - 1;
        for(int i = A.size() - 1; i >= 0; i--) {
            if(B[i] >= A[right])
            {
                m[i] = A[left++];                
            }
            else
                m[i] = A[right--];
            cout << B[i] << " " << m[B[i]] << endl;
        }
        vector<int> res;
        for(auto& num:C)
        {
            res.push_back(m[num]);
        }
        return res;
    }
};
